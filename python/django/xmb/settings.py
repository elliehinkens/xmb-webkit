"""
Django settings for playstation project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import sys
from pathlib import Path
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath('.'), 'config.ini'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(os.path.abspath('.'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'playstation',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'playstation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'playstation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
BASE_URL = 'http://127.0.0.1:8000/'

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    CHROMIUM_PATH = os.path.join(os.path.abspath("."), 'chromium/chrome.exe')
else:
    CHROMIUM_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath("."))), 'release/chromium/chrome.exe')

WEB_ASSETS_PATH = 'webassets' + os.sep
ROMS_PATH = config.get('PATH', 'ROMS_PATH')
SYS_IMAGE_PATH = 'img' + os.sep + 'sys-icon' + os.sep
TICK_SONG_PATH = 'audio' + os.sep + 'tick.mp3'
ROMS_MEDIA_DIRECTORY = 'media'
ROMS_IMAGE_DIRECTORY = 'box2dfront'
ROMS_3D_IMAGE_DIRECTORY = 'box3d'
ROMS_VIDEO_DIRECTORY = 'videos'
NO_IMAGE_PATH = 'img' + os.sep + 'No Image.png'
NO_VIDEO_PATH = 'video' + os.sep + 'No Video.mp4'

STATIC_URL = 'static/playstation/'
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    STATIC_PATH = os.path.join(os.path.abspath("."), WEB_ASSETS_PATH)
    if os.path.exists(ROMS_PATH):
        STATICFILES_DIRS = (
            STATIC_PATH,
            ROMS_PATH,
        )
    else:
        STATICFILES_DIRS = (
            STATIC_PATH,
        )
else:
    STATIC_PATH = os.path.join(os.path.abspath("."), STATIC_URL)
    if os.path.exists(ROMS_PATH):
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, STATIC_URL),
            ROMS_PATH,
        )
    else:
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, STATIC_URL),
        )

    
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ROM_EXEC_COMMANDS = {
    'gc': config.get('ROM_EXE_PATH', 'gc'),
    'n64': config.get('ROM_EXE_PATH', 'n64'),
    'nes': config.get('ROM_EXE_PATH', 'nes'),
    'ps1': config.get('ROM_EXE_PATH', 'ps1'),
    'ps2': config.get('ROM_EXE_PATH', 'ps2'),
    'snes': config.get('ROM_EXE_PATH', 'snes'),
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'