"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import environ
import django_heroku
from typing import List, Dict, Any


BASE_DIR: str = Path(__file__).resolve().parent.parent
SECRET_KEY: str = env('SECRET_KEY')
DEBUG: str = env('DEBUG')
ALLOWED_HOSTS: List[str] = env('ALLOWED_HOSTS').split(',')

env: environ.Env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()


# Application definition
INSTALLED_APPS: List[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'user',
    'core',
    'data',
    'home',
]

MIDDLEWARE: List[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF: str = 'app.urls'


# This project contains limited templates.
# TEMPLATES's Dict value can contain types like str,
# True, Dict, list and other types too.
TEMPLATES: Dict[str, Any] = [
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

WSGI_APPLICATION: str = 'app.wsgi.application'


# Database info can be found at: 
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
if DEBUG:
    DB_NAME: str = BASE_DIR / env('DB_NAME')
else:
    DB_NAME: str = env('DB_NAME')

DATABASES: Dict[str, str] = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME':  DB_NAME,
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
# Currently using default settings for this project.
AUTH_PASSWORD_VALIDATORS: List[Dict[str, str]] = [
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# Currently we have no plan for Internationalization:-
# Because we are using third party package (beautiful soup)
# to parse data for API. 
LANGUAGE_CODE: str = 'en-us'
TIME_ZONE: str = 'UTC'
USE_I18N: bool = True
USE_TZ: bool = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL: str = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'
AUTH_USER_MODEL: str = 'core.user'

STATIC_ROOT: str = os.path.join(BASE_DIR, 'static')

# Activate Django-Heroku.
django_heroku.settings(locals())
