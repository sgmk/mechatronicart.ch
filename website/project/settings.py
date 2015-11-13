import os
import sys

from colorlog import ColoredFormatter


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

ALLOWED_HOSTS = ['*',]
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'gunicorn',
    'django_extensions',
    'compressor',
    'sass_processor',
    'sekizai',
    'tastypie',
    'lineage',
    'adminsortable',
    'taggit',
    'taggit_templatetags',
    #'easy_thumbnails',              # dependency for filer
    #'mptt',                         # dependency for filer
    #'filer',
    'django_markdown',
    'sorl.thumbnail',               # dependency for newsletter
    'newsletter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
     # enable messages
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static configuration
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),]
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'site-static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FILES_ROOT = os.path.join(BASE_DIR, 'media/files')
FILES_URL = '/media/files/'


THUMBNAIL_BASEDIR = 'files'

# filer
FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(BASE_DIR, 'media/files'),
                'base_url': '/media/files/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(BASE_DIR, 'media/files'),
                'base_url': '/media/files/',
            },
        },
    },
}

# tastypie
API_VERSION = 'v1'
TASTYPIE_ALLOW_MISSING_SLASH = True


# sass
SASS_PROCESSOR_INCLUDE_DIRS = (
    os.path.join(BASE_DIR, 'scss'),
    os.path.join(BASE_DIR, 'site-static/bower_components/foundation/scss'),
)

SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'site-static')


# messages
from django.contrib.messages import constants as messages
# override messsages tags for foundation.css
MESSAGE_TAGS = {
    messages.ERROR: 'alert',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': "%(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(lineno)-4s%(name)-32s %(levelname)-8s %(message)s',
            'log_colors': {
                'DEBUG': 'bold_black',
                'INFO': 'white',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'WARNING',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django-warning.log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'simple',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'colored'
        },
    },
    'loggers': {
        'modx_legacy': {
            'handlers': ['console',],
            'propagate': False,
            'level': 'DEBUG',
        },
        'requests': {
            'handlers': ['console', 'logfile'],
            'propagate': False,
            'level': 'ERROR',
        },
        'django': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
            'level': 'ERROR',
        },
        'django.request': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}


# load local_settings
try:
    from local_settings import *
except ImportError:
    pass
