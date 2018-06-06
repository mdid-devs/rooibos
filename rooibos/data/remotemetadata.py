import urllib2
import logging
import shutil
import os
import string
import random
import gzip
import StringIO
from celery import chain
from django.contrib.auth.models import User
from rooibos.storage.tasks import storage_match_up_media
from .models import RemoteMetadata
from .spreadsheetimport import create_import_job
from .views import _get_scratch_dir


logger = logging.getLogger(__name__)


def check_remote_metadata():
    sources = RemoteMetadata.objects.all()
    for source in sources:
        logger.info(
            'Checking remote metadata %d at "%s", last modified "%s"' %
            (source.id, source.url, source.last_modified)
        )
        try:
            request = urllib2.Request(source.url)
            request.get_method = lambda : 'HEAD'
            response = urllib2.urlopen(request)
        except Exception:
            logger.exception(
                'Error while fetching HEAD for RemoteMetadata '
                '%d at "%s"' % (source.id, source.url)
            )
            continue
        last_modified = response.info()['Last-Modified']
        if last_modified != source.last_modified:
            logger.info(
                'Remote metadata %d updated "%s"' %
                (source.id, last_modified)
            )
            source.last_modified = last_modified
            yield source
        else:
            logger.info(
                'Remote metadata %d unchanged' % source.id
            )


def fetch_url_to_file(url, path):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    except Exception:
        logger.exception(
            'Error while fetching URL "%s"' % url
        )
        return False

    remote = StringIO.StringIO(response.read())
    if url.endswith('.gz'):
        remote = gzip.GzipFile(fileobj=remote, mode='rb')
    with open(path, 'wb') as outfile:
        shutil.copyfileobj(remote, outfile)
    logger.info(
        'URL "%s" downloaded to "%s"' % (url, path)
    )
    return True


def fetch_remote_metadata():
    for source in check_remote_metadata():
        filename = "".join(random.sample(string.letters + string.digits, 32))
        full_metadata_path = os.path.join(
            _get_scratch_dir(), 'remote-metadata=' + filename)
        full_mapping_path = os.path.join(
            _get_scratch_dir(), 'remote-mapping=' + filename)

        if fetch_url_to_file(source.url, full_metadata_path) and \
                fetch_url_to_file(source.mapping_url, full_mapping_path):
            import_metadata = create_import_job(
                full_mapping_path, full_metadata_path, [source.collection_id])

            match_up_media = storage_match_up_media.si(
                owner=User.objects.get(username='admin').id,
                storage_id=source.storage_id,
                collection_id=source.collection_id,
                allow_multiple_use=False)

            task = chain(import_metadata, match_up_media).delay()

            source.save()

            logger.info(
                'Submitted import job for remote metadata %d with task %s' %
                (source.id, task.id)
            )
