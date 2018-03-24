# -*- coding: utf-8 -*-
import os
DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = ')dq%h#fuqfr-zt8#o=_o&*6r^(=g-3o*6p4mi8--z_8n@3x2*#'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taskmanager',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

ROOT_URLCONF = 'taskmanager.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'taskmanager.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

LANGUAGE_CODE = 'cs'
TIME_ZONE = 'UTC'
USE_I18N = True

USE_L10N = True
USE_TZ = True
STATIC_URL = '/api/static/'
STATIC_ROOT = BASE_DIR + "/static/"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + "/media/"

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'taskmanager': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'taskmanager.log',
            'formatter': 'taskmanager',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    },
}
