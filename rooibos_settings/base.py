# DON'T PUT ANY LOCALIZED SETTINGS OR SECRETS IN THIS FILE
# they should go in a custom file instead based on settings/template.py

import os
import sys
import re


install_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

if install_dir not in sys.path:
    sys.path.insert(0, install_dir)


DEBUG = False
TEMPLATE_DEBUG = DEBUG


# Needed to enable compression JS and CSS files
COMPRESS = True
COMPRESS_VERBOSE = True


STATIC_ROOT = os.path.join(install_dir, '..', 'static')

SCRATCH_DIR = os.path.join(install_dir, '..', 'scratch')
AUTO_STORAGE_DIR = os.path.join(install_dir, '..', 'autostorage')


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

DEFAULT_LANGUAGE = 'en-us'


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

USE_ETAGS = False

# When set to True, may cause problems with basket functionality
SESSION_SAVE_EVERY_REQUEST = False


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media-unused/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "rooibos.context_processors.settings",
    "rooibos.context_processors.selected_records",
    "rooibos.context_processors.current_presentation",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.http.ConditionalGetMiddleware',
    'rooibos.middleware.Middleware',
    'rooibos.help.middleware.PageHelp',
    'rooibos.sslredirect.SSLRedirect',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'rooibos.api.middleware.CookielessSessionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'rooibos.ui.middleware.PageTitles',
    'pagination.middleware.PaginationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'rooibos.storage.middleware.StorageOnStart',
    'rooibos.access.middleware.AccessOnStart',
    'rooibos.data.middleware.DataOnStart',
    'rooibos.middleware.HistoryMiddleware',
    'rooibos.access.middleware.AnonymousIpGroupMembershipMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'rooibos.auth.middleware.BasicAuthenticationMiddleware',
)


ROOT_URLCONF = 'rooibos.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.comments',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_extensions',
    'tagging',
    'google_analytics',
    'rooibos.data',
    'rooibos.migration',
    'rooibos.util',
    'rooibos.access',
    'rooibos.solr',
    'rooibos.storage',
    'rooibos.legacy',
    'rooibos.ui',
    'rooibos.viewers',
    'rooibos.help',
    'rooibos.presentation',
    'rooibos.statistics',
    'rooibos.federatedsearch',
    'rooibos.federatedsearch.artstor',
    'rooibos.federatedsearch.flickr',
    'rooibos.federatedsearch.shared',
    'rooibos.workers',
    'rooibos.userprofile',
    'rooibos.mediaviewer',
    'rooibos.megazine',
    'rooibos.groupmanager',
    'rooibos.pdfviewer',
    'rooibos.pptexport',
    'rooibos.works',
    'pagination',
    'impersonate',
    'compressor',
    'south',
)


STORAGE_SYSTEMS = {
    'local': 'rooibos.storage.localfs.LocalFileSystemStorageSystem',
    'online': 'rooibos.storage.online.OnlineStorageSystem',
    'pseudostreaming':
        'rooibos.storage.pseudostreaming.PseudoStreamingStorageSystem',
    's3': 'rooibos.storage.s3.S3StorageSystem',
}

GROUP_MANAGERS = {
}

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

WEBSERVICE_NAMESPACE = "http://mdid.jmu.edu/webservices"

# Methods to be called after a user is successfully authenticated
# using an external backend (LDAP, IMAP, POP).
# Must take two parameters:
#   user object
#   dict of string->list/tuple pairs (may be None or empty)
# Returns:
#   True: login continues
#   False: login rejected, try additional login backends if available
LOGIN_CHECKS = (
    'rooibos.access.models.update_membership_by_attributes',
)

TEMPLATE_DIRS = (
    os.path.join(install_dir, 'rooibos', 'templates'),
)

STATICFILES_DIRS = [
    os.path.join(install_dir, 'rooibos', 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_URL = '/static/'


FFMPEG_EXECUTABLE = '/usr/local/bin/ffmpeg'

PDF_PAGESIZE = 'letter'  # 'A4'

SHOW_FRONTPAGE_LOGIN = "yes"

MASTER_TEMPLATE = 'master_root.html'


ARTSTOR_GATEWAY = None


LOGO_URL = None
FAVICON_URL = None
COPYRIGHT = None
TITLE = None

HIDE_SHOWCASES = False


PPTEXPORT_WIDTH = 800
PPTEXPORT_HEIGHT = 600


COMPACT_METADATA_VIEW = False

WORKS = {
    'EXPLORE_MENU': False,
    'SEARCH_BOX': False,
}


FLICKR_KEY = ''
FLICKR_SECRET = ''


CUSTOM_TRACKER_HTML = ""

SHOW_FRONTPAGE_LOGIN = 'yes'


# The Megazine viewer is using a third party component that has commercial
# licensing requirements.  To enable the component you need to enter your
# license key, which is available for free for educational institutions.
# See static/megazine/COPYING.
MEGAZINE_PUBLIC_KEY = ""

# To use a commercial licensed flowplayer, enter your flowplayer key here
# and add the flowplayer.commercial-3.x.x.swf file to the
# rooibos/static/flowplayer directory
FLOWPLAYER_KEY = ""


# By default, video delivery links are created as symbolic links. Some
# streaming servers (e.g. Wowza) don't deliver those, so hard links are
# required.
HARD_VIDEO_DELIVERY_LINKS = False


# List of facets to permanently hide in Explore screen
# Comparison is made on effective (shown) label
HIDE_FACETS = ()
# List of facets using whole expression instead of tokenized terms
# Comparison is made on effective (shown) label
FULL_FACETS = ()


PREVIEW_WIDTH = 640
PREVIEW_HEIGHT = 480


# If the JPEGs available to MDID are not compressed properly, loading a
# presentation may take a very long time, as a lot of large images have to be
# transferred.  By setting this, presentation images are forces to be
# reprocessed and compressed to the usual 85% quality
FORCE_SLIDE_REPROCESS = False


# If set to a list of strings, all groups with the given names are granted read
# access on newly created presentations
PRESENTATION_PERMISSIONS = []


# Show extra field values next to thumbnails, specify by field label
# THUMB_EXTRA_FIELDS = ['Creator', 'Work Type']
THUMB_EXTRA_TEMPLATE = 'ui_record_extra.html'
THUMB_EXTRA_FIELDS = []


# Settings that should be available in template rendering
EXPOSE_TO_CONTEXT = (
    'STATIC_DIR',
    'PRIMARY_COLOR',
    'SECONDARY_COLOR',
    'CUSTOM_TRACKER_HTML',
    'ADMINS',
    'LOGO_URL',
    'FAVICON_URL',
    'COPYRIGHT',
    'TITLE',
    'SHOW_FRONTPAGE_LOGIN',
    'MASTER_TEMPLATE',
    'PREVIEW_WIDTH',
    'PREVIEW_HEIGHT',
    'SHOW_TERMS',
    'SHIB_ENABLED',
    'SHIB_LOGOUT_URL',
    'HIDE_SHOWCASES',
    'CAS_SERVER_URL',
    'WORKS',
)


ADMINS = (
    # ('Your name', 'your@email.example'),
)

MANAGERS = ADMINS


GOOGLE_ANALYTICS_MODEL = True


INSTANCE_NAME = ''


LDAP_AUTH = ()
IMAP_AUTH = ()
POP3_AUTH = ()

SHIB_ENABLED = False
SHIB_ATTRIBUTE_MAP = None
SHIB_USERNAME = None
SHIB_EMAIL = None
SHIB_FIRST_NAME = None
SHIB_LAST_NAME = None
SHIB_LOGOUT_URL = None

SSL_PORT = None  # ':443'

SESSION_COOKIE_AGE = 6 * 3600  # in seconds


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': INSTANCE_NAME,
    }
}


INTERNAL_IPS = ('127.0.0.1', )


# If HELP_URL ends in / or ?, the current page id or reference will be appended
HELP_URL = 'http://mdid.org/help/'


# S3 settings
S3_FOLDER_MAPPING = {}
AWS_STORAGE_BUCKET_NAME = ''
AWS_ACCESS_KEY = None
AWS_SECRET_KEY = None

CDN_THUMBNAILS = {}

UPLOAD_LIMIT = 5 * 1024 * 1024


CAS_SERVER_URL = None


WWW_AUTHENTICATION_REALM = "Please log in to access media from MDID " \
    "at Your University"


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'rooibos.auth.ldapauth.LdapAuthenticationBackend',
    'rooibos.auth.mailauth.ImapAuthenticationBackend',
    'rooibos.auth.mailauth.PopAuthenticationBackend',
)


MASTER_TEMPLATE = 'master_root.html'


def _get_log_handler(log_dir=None):

    # Can't do sys.argv since it does not exist when running under PyISAPIe
    cmdline = getattr(sys, 'argv', [])
    if len(cmdline) > 1:
        # only use first command line argument for log file name
        basename = 'rooibos-%s' % '-'.join(
            re.sub(r'[^a-zA-Z0-9]', '', x) for x in cmdline[1:2])
    else:
        basename = 'rooibos'

    if not log_dir:
        log_dir = os.path.join(install_dir, '..', 'log')

    return {
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_dir, basename +'.log'),
            'formatter': 'verbose',
        },
    }


handler = _get_log_handler()
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(name)30.30s]%(levelname)8s %(asctime)s '
                      '%(process)d %(message)s '
                      '[%(filename)s:%(lineno)d]'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': handler,
    'loggers': {
        'rooibos': {
            'handlers': [handler.keys()[0]],
            'level': 'DEBUG',
            'propagate': False,
        },
        'pika': {
            'handlers': [handler.keys()[0]],
            'level': 'WARNING',
        },
        '': {
            'handlers': [handler.keys()[0]],
            'level': 'DEBUG',
        },
    },
}