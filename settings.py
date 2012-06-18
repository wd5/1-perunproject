# -*- coding: utf-8 -*-

# project settings, Django 1.3 required

import os
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__)) 

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
LANGUAGE_CODE = 'ru'

#APPEND_SLASH = False #default True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

USER_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '../static/')
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.csrf',
    'django.core.context_processors.request',
    'mezzanine.conf.context_processors.settings',
    #'djangobb_forum.context_processors.forum_settings',
    #'simplepages.context_processors.page',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'dbtemplates.loader.Loader',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates/'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    #'djangobb_forum.middleware.LastLoginMiddleware',
    #'djangobb_forum.middleware.UsersOnline',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'simplepages.middleware.PageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'subdomains.SubdomainMiddleware',
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.staticfiles',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sitemaps',

    'django.contrib.markup',

    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    #'mezzanine.blog',
    'mezzanine.forms',
    'mezzanine.pages',
    'mezzanine.galleries',
    #'mezzanine.twitter',
    #"mezzanine.accounts",
    #"mezzanine.mobile",
    'mezzanine_wiki',

    #'south',
    'dbtemplates',
    'registration',
    'avatar',
    'profiles',
    'sorl.thumbnail', #'easy_thumbnails',
    'tagging',
    'captcha',
    'netauth',
    'form_utils',
    'genericadmin',
    'basic.inlines',
    'pagination',
    #'syncr.youtube',

    #'haystack',
    #'djangobb_forum',
    #'messages',

    'simplepages',
    'fblog',
    'fgallery',
    'fevents',
    'fshop',
    'cart',
    'mptt',

    'fcss',
    'fcomments',
    'perunstyle',
    'perunprofile',
    'perunutils',

    'seo',
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}

try:
    import mailer
    INSTALLED_APPS += ('mailer',)
    EMAIL_BACKEND = "mailer.backend.DbBackend"
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


# =========================== APP SETTINGS ===========================

AUTHENTICATION_BACKENDS = (
    'netauth.auth.NetBackend',
    #'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, '../data/fixtures/'),
)

# Account settings
ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

AUTH_PROFILE_MODULE = 'perunprofile.UserProfile'

AVATAR_DEFAULT_SIZE = 60
AVATAR_THUMB_QUALITY = 95
AUTO_GENERATE_AVATAR_SIZES = (60, 80,)

#Cache settings
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

COMMENTS_APP = "fcomments"

THUMBNAIL_QUALITY = 90

CAPTCHA_BACKGROUND_COLOR = '#000000'
CAPTCHA_FOREGROUND_COLOR = '#cccccc'

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS = ''
#CAPTCHA_FILTER_FUNCTIONS = ''
CAPTCHA_LETTER_ROTATION = (-15,15)

SEO_FOR_MODELS = [
    'simplepages.models.Page',
    'fblog.models.Post',
    'fgallery.models.Photo',
    'fgallery.models.Album',
]

WIKI_DEFAULT_INDEX = 'Академия'

FBLOG_BLOG_TITLE = 'Дневник клуба "Стрелы Перуна"'

DJANGOBB_FORUM_BASE_TITLE = 'Форум Перуновой Слободы'
DJANGOBB_HEADER = 'Перунова Слобода'
DJANGOBB_TAGLINE = 'Перунова Слобода - клановое бойцовское поселение клуба СГБ "Стрелы Перуна"'
DJANGOBB_TOPIC_PAGE_SIZE = 20

# Haystack settings
HAYSTACK_SITECONF = 'search_sites'
HAYSTACK_SEARCH_ENGINE = 'dummy'
HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_DIR, 'djangobb_index')

FSHOP_SHOP_TITLE = 'Гильдия мастеров'


# ========================== MEZZANINE SETTINGS ==========================

USE_SOUTH = False



# ============================ LOCAL SETTINGS ============================

import socket
if socket.gethostname() == 'hydrogen':
    #DEBUG = False
    from password import *
    LOCALSERVER = False
else:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    from local_settings import *

from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())
