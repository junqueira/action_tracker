"""
Django settings for active_tracker project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django import template

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#w3ru7u6dy8vx)9d#z*@$vydcscs7&hg-p)pfa7%w$ih)&3lf*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

PROJECT_APPS = (
    'tracker',
    'public',
    'users',
    'dashboard',
)

THIRDY_APPS = (
    'djangular',
)

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRDY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'active_tracker.urls'

WSGI_APPLICATION = 'active_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'active_tracker.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# TASTYPIE
TASTYPIE_FULL_DEBUG = True
API_LIMIT_PER_PAGE = 100
TASTYPIE_ALLOW_MISSING_SLASH = False
TASTYPIE_DEFAULT_FORMATS = ['json']

# Local settings
try:
    settings_local = os.path.join(BASE_DIR, 'active_tracker', 'settings_local.py')
    execfile(settings_local)
except IOError:
    pass


# Context processors ( Global variables for templates )
TEMPLATE_CONTEXT_PROCESSORS += (
    # FIXME: this is one security fail, you can import requests, get or post
    "common.context_processors.global_vars",
)

# Autoload i18n tag in all templates
template.add_to_builtins('common.filters')

