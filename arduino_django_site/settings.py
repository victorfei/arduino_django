"""
Django settings for arduino_django_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import urlparse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
 
# Dynamically define where the project root is.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2u8pe%5b^1bg=!#1skz4za%*%mf8#7%=&@4oofa5gy%!w#ji_y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'email_usernames',
    'users',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'arduino_django_site.urls'

WSGI_APPLICATION = 'arduino_django_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# commented out for heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arduino_django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = [
    'eneura.herokuapp.com',
]


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/') 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

# For some reasons, if I put bootstrap files under 'static' folder and run 'python manage.py collectstaic'
# I can't render the bootstrap files. But if I place it somewhere else like 'templates' folder,
# I can then run 'collectstatic'
STATICFILES_DIRS =(
    os.path.join(PROJECT_ROOT, 'templates/bootstrap'),
)

# to use UserProfile model defined in application users
AUTH_PROFILE_MODULE = 'users.UserProfile'

# below settings are used for account registration.
ACCOUNT_ACTIVATION_DAYS = 7

# Specifiy what page to go to once the user is logged in.
LOGIN_REDIRECT_URL = '/profile'

# ---------------Heroku-----------------
import dj_database_url
# leaving this line on heroku wouldn't work
DATABASES['default'] =  dj_database_url.config()
# dj_database_url.config(os.environ['DATABASE_URL'])

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

## Register database schemes in URLs.
#urlparse.uses_netloc.append('mysql')
#
#try:
#
#    # Check to make sure DATABASES is set in settings.py file.
#    # If not default to {}
#
#    if 'DATABASES' not in locals():
#        DATABASES = {}
#
#    if 'DATABASE_URL' in os.environ:
#        url = urlparse.urlparse(os.environ['DATABASE_URL'])
#
#        # Ensure default database exists.
#        DATABASES['default'] = DATABASES.get('default', {})
#
#        # Update with environment configuration.
#        DATABASES['default'].update({
#            'NAME': url.path[1:],
#            'USER': url.username,
#            'PASSWORD': url.password,
#            'HOST': url.hostname,
#            'PORT': url.port,
#        })
#
#
#        if url.scheme == 'mysql':
#            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
#except Exception:
#    print 'Unexpected error:', sys.exc_info()
#
# -------------------------add your changes above this line-----------------
# This essentially allows the database setting in 
# local_settings.py (../arduino_django/local_settings) to overwrite the database
# settings in the current file (settings.py), so to avoid database setting 
# conflicts can be avoid when different people are commiting to GIT. 
try:
    from local_settings import *
except ImportError:
    pass
