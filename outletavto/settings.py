"""
Django settings for outletavto project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import listdir
from os.path import isfile, join
import os
import mimetypes

mimetypes.add_type("text/css", ".css")
mimetypes.add_type("image/svg+xml", ".svg")

BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p)ophp_2lp@h27(jlomu&%v64lq=s%$_c6mv(&tzqeu=npim54'



ALLOWED_HOSTS = ['xn--061-3edaa.xn--p1ai','outletavto-shamemask.b4a.run','127.0.0.1','5.63.155.57','outletavto.ru']


# Application definition

SITE_ID = 2

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # for Google OAuth 2.0
    'sass_processor',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '221643686649-653ssl4p5eba6hfimrv1lgmul2otq593.apps.googleusercontent.com',
            'secret': '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',
            'key': '',
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False,
        'redirect_uri': 'https://outletavto.ru/accounts/google/login/callback/',
    },
    'yandex': {
        'APP': {
            'client_id': 'your-yandex-client-id',
            'secret': 'your-yandex-client-secret',
            'key': '',
        },
        'SCOPE': [
            'login:email',
            'login:info',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_TRUSTED_ORIGINS = ['http://5.63.155.57','https://outletavto.ru']  # Замените на свой домен или IP-адрес
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'  # Укажите хост вашего почтового сервера
EMAIL_PORT = 2525  # Порт сервера
EMAIL_HOST_USER = 'snab061@bk.ru'  # Укажите вашу почту
EMAIL_HOST_PASSWORD = '4iK3EhQbnijKysFDmGyT'  # Укажите пароль от вашей почты
EMAIL_USE_TLS = True  # Использовать TLS для безопасного соединения
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'snab061@bk.ru'  # Укажите почту отправителя
ROOT_URLCONF = 'outletavto.urls'

if str(BASE_DIR) == 'C:\projOutlet\outletavto2':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'outletavto',
            'USER': 'admin',
            'PASSWORD': 'yfMhL7PiOB30M9WN',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'outletavto',
            'USER': 'admin',
            'PASSWORD': 'yfMhL7PiOB30M9WN',
            'HOST': 'db',
            'PORT': '5432',
        }
    }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR2, 'static/outletauto')],
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

WSGI_APPLICATION = 'outletavto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
print(str(BASE_DIR) == 'C:\projOutlet\outletavto2')
if str(BASE_DIR) == 'C:\projOutlet\outletavto2':
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "images"),
    ]

# onlyfiles = [f for f in listdir(os.path.join(BASE_DIR, "static")) if isfile(join(os.path.join(BASE_DIR, "static"), f))]
# print(onlyfiles)
else:
    STATIC_ROOT = '/srv/www/outletavto/static/'
    DEBUG = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'