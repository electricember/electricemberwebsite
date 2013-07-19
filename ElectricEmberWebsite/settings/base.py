#################################################
# Django base settings for ElectricEmberWebsite project.
import os
from unipath import Path

# Normally you shouldn't import ANYTHING from Django directly into settings,
#   but ImproperlyConfigured is one rare exception
from django.core.exceptions import ImproperlyConfigured
msg = "Set the %s environment variable."
# get_env_variable(var_name)
# Can be used to attempt to access an environment variable, and if it is unavailable,
#   gives a more useful error message and traceback so the variable can be set by a
#   sysadmin.
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = msg % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

# Set this_file to  '/path/to/electricemberwebsite/ElectricEmberWebsite/settings/base.py'
#   so that other important directories can be defined relative to it.
this_file = Path(__file__).absolute()
PROJECT_DIR = this_file.ancestor(3)  # PROJECT_DIR = '/path/to/electricemberwebsite/'
PROJECT_APPS_DIR = PROJECT_DIR.child("ElectricEmberWebsite")
MEDIA_ROOT = PROJECT_APPS_DIR.child("media")
STATIC_ROOT = PROJECT_APPS_DIR.child("static")
TEMPLATE_DIRS = (
    PROJECT_APPS_DIR.child("templates"),
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
#    (PROJECT_APPS_DIR.child("static").child("bootstrap").child("js")),
    PROJECT_APPS_DIR.child("static"),
)

ADMINS = (
    ('shawn', 'shawn.furyan@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ElectricEmberWebsite', # db_name
        'USER': 'django', # db_user
        #'PASSWORD: 'db_user_password', # db_user_passwd
        'HOST': ''
        #'PORT': '',                      # Set to empty string for default.
        #'OPTIONS': {}
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [ '99.64.102.64', '127.0.0.1', ]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
#SECRET_KEY = 'ked=7&yp_7+oa@0sk7(=v2a$k0%v5=(6#m&f_w@2xvj%t+9a3@'
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ElectricEmberWebsite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ElectricEmberWebsite.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'django.contrib.admin',
     'django.contrib.admindocs',
     'south',
     'landing',
     'products',
     #'homepage',
     #'polls',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
