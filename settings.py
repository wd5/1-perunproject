# -*- coding: utf-8 -*-

# Django settings for djbase project.

import os
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin', 'contact@perunspace.ru'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

#APPEND_SLASH = False #default True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
MEDIA_ROOT = '/home/hosting_dfalk/projects/perunspace/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.csrf',
    'django.core.context_processors.request',
    #'django_authopenid.context_processors.authopenid',
    'djangobb_forum.context_processors.forum_settings',
    #'simplepages.context_processors.page',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'djangobb_forum.middleware.LastLoginMiddleware',
    'djangobb_forum.middleware.UsersOnline',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'simplepages.middleware.PageFallbackMiddleware',
    'subdomains.SubdomainMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/hosting_dfalk/projects/perunspace/app/templates/',
)

FIXTURE_DIRS = (
    '/home/hosting_dfalk/projects/perunspace/data/fixtures/',
)

INSTALLED_APPS = (
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.contenttypes',

    'django.contrib.markup',

    'registration',
    'sorl.thumbnail',
    #'easy_thumbnails',
    'tagging',
    'djangobb_forum',
    'haystack',
    'messages',
    'captcha',
    'netauth',
    'syncr.youtube',

    'simplepages',
    'basic.inlines',
    'fblog',
    'fgallery',
    'fevents',
    'fcomments',
)

COMMENTS_APP = "fcomments"

THUMBNAIL_QUALITY = 90

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS = ''
#CAPTCHA_FILTER_FUNCTIONS = ''
CAPTCHA_LETTER_ROTATION = (-15,15)

try:
    import mailer
    INSTALLED_APPS += ('mailer',)
    EMAIL_BACKEND = "mailer.backend.DbBackend"
except ImportError:
    pass

try:
    import south
    INSTALLED_APPS += ('south',)
    SOUTH_TESTS_MIGRATE = False
except ImportError:
    pass

# SECRET_KEY
if not hasattr(globals(), 'SECRET_KEY'):
    SECRET_FILE = os.path.join(PROJECT_DIR, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            import string
            symbols = ''.join((string.lowercase, string.digits, string.punctuation ))
            SECRET_KEY = ''.join([choice(symbols) for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            raise Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)

DJANGOBB_FORUM_BASE_TITLE = 'Форум Перуновой Слободы'
DJANGOBB_HEADER = 'Перунова Слобода'
DJANGOBB_TAGLINE = 'Перунова Слобода - клановое бойцовское поселение клуба СГБ "Стрелы Перуна"'

# Haystack settings
HAYSTACK_SITECONF = 'search_sites'
HAYSTACK_SEARCH_ENGINE = 'dummy'
HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_DIR, 'djangobb_index')

# Account settings
ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

#Cache settings
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

AUTHENTICATION_BACKENDS = (
    'netauth.auth.NetBackend',
    #'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# LOCAL SETTINGS
import socket
if socket.gethostname() == 'hydrogen':
    #DEBUG = False
    from password import *
    LOCALSERVER = False
else:
    #DEBUG = True
    from local_settings import *
