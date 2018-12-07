"""
Django settings for zhem project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_fcw2t6u_sv@bn^!jxpp3sb_bb3g&+3*gpsp0bun&ij9=d)v=s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['77.222.63.160']


# Application definition

INSTALLED_APPS = [
    #'jet',
    'material.theme.blue',
    'material',
    'material.admin',
    'material.frontend',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crm.apps.CrmConfig',
    'zvonki.apps.ZvonkiConfig',
    'django_cleanup',
    'phonenumber_field',
    'el_pagination',
    'multiselectfield',
    'datetimepicker',
    'reset_migrations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'zhem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'crm.context_processors.main',
            ],
        },
    },
]

WSGI_APPLICATION = 'zhem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
DEFAULT_CHARSET = 'utf-8'
TIME_ZONE = 'Europe/Moscow'
SESSION_COOKIE_AGE = 7680

USE_I18N = True
USE_L10N = True
USE_TZ = True

EL_PAGINATION_PER_PAGE = 15
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#STATIC_PATH = os.path.join(BASE_DIR, 'static')
#STATIC_URL = '/static/'

MEDIA_ROOT = '/var/www/crm/crm/'
MEDIA_URL = '/'

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'zhem-otchet@mail.ru'
EMAIL_HOST_PASSWORD = 'nokia2012'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/var/www/crm/crm/static/stat/'
STATIC_URL = '/static/stat/'

#STATICFILES_DIRS = (
#	'/var/www/crm/crm/static/stat/',
#)
