# -*- coding: utf-8 -*-

# perunspace project settings, Django 1.3+ required
# based on Mezzanine CMS

#_ = lambda s: s
from django.utils.translation import ugettext_lazy as _

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
    #'dbtemplates.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates/'),
)

MIDDLEWARE_CLASSES = (
    #'mezzanine.core.middleware.UpdateCacheMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    #'django.middleware.transaction.TransactionMiddleware',
    #'djangobb_forum.middleware.LastLoginMiddleware',
    #'djangobb_forum.middleware.UsersOnline',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'simplepages.middleware.PageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'subdomains.SubdomainMiddleware',
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    #"mezzanine.core.middleware.FetchFromCacheMiddleware",
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    ## core apps
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.contenttypes',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.markup',

    ## theme apps
    'perunstyle',

    ## cms apps
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

    ## project apps
    'fblog',
    'fgallery',
    'fevents',
    'mezzanine_wiki',
    'fcomments',
    'perunprofile',

    ## project utils
    'sorl.thumbnail', # legacy 3.2.5
    'tagging',
    'captcha',
    'netauth',
    'form_utils',
    'genericadmin',
    'inlines',
    'pagination',
    'perunutils',

    ## deprecate in version 0.3

    ## accounts, replace with userena
    'registration',
    'avatar',
    'profiles',

    ## forum, temporary deleted
    #'djangobb_forum',
    #'haystack',
    #'messages',

    ## shop
    'fshop', # replace with cartridge
    'cart',
    'mptt',

    ## other
    #'simplepages', # replace with mezzanine
    #'fcss',
    #'dbtemplates', # replace with templateadmin
    #'seo',
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

INTERNAL_IPS = ("127.0.0.1",)

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
    #'django.contrib.auth.backends.ModelBackend',
    'mezzanine.core.auth_backends.MezzanineBackend',
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

WIKI_DEFAULT_INDEX = 'Академия'

FBLOG_BLOG_TITLE = 'Дневник клуба "Стрелы Перуна"'

FSHOP_SHOP_TITLE = 'Гильдия мастеров'


# ========================== MEZZANINE SETTINGS ==========================

USE_SOUTH = True

ADMIN_MENU_ORDER = (
    (_("Content"), ("pages.Page", "fblog.Post", "fevents.Event", 
       "fgallery.Album", "mezzanine_wiki.WikiPage",
       "generic.ThreadedComment", "comments.Comment",
       (_("Media Library"), "fb_browse"),)),
    (_("Shop"), ("shop.Product", "shop.ProductVariation", "shop.Vendor",
              "shop.DiscountCode", "shop.Sale", "shop.Order",
              "customshop.Shipping", "customshop.Payment",)),
    (_("Site"), ("sites.Site", "redirects.Redirect", "conf.Setting")),
    (_("Users"), ("auth.User", "auth.Group",
       "perunprofile.UserProfile", "registration.RegistrationProfile",
       "netauth.NetID", "avatar.Avatar")),
    (_("Other"), ("inlines.InlineType", "fblog.Ptype",
       "fevents.Etype", "fgallery.Video", "fgallery.Photo",
       "tagging.Tag", "tagging.TaggedItem")),
)

TEMPLATE_ACCESSIBLE_SETTINGS = (
    "ACCOUNTS_VERIFICATION_REQUIRED", "ADMIN_MEDIA_PREFIX",
    "BLOG_BITLY_USER", "BLOG_BITLY_KEY",
    "COMMENTS_DISQUS_SHORTNAME", "COMMENTS_NUM_LATEST",
    "COMMENTS_DISQUS_API_PUBLIC_KEY", "COMMENTS_DISQUS_API_SECRET_KEY",
    "DEV_SERVER", "FORMS_USE_HTML5", "GRAPPELLI_INSTALLED",
    "GOOGLE_ANALYTICS_ID", "JQUERY_FILENAME", "LOGIN_URL", "LOGOUT_URL",
    "PAGES_MENU_SHOW_ALL", "SITE_TITLE", "SITE_TAGLINE", "RATINGS_MAX",
    "SITE_SLOGAN",
)


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
