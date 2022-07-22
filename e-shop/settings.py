"""
Django settings for shoppinglyx project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.core.mail import send_mail  

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8o353)z(_*^04+jhey!m*q3_no@vhn*7v8(6xz4rl6=kunu=it'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
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

ROOT_URLCONF = 'shoppinglyx.urls'

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

WSGI_APPLICATION = 'shoppinglyx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# changing default url of login submit page
LOGIN_REDIRECT_URL = '/profile/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_HOST_USER = 'yashasvimahajan276@gmail.com'  
EMAIL_HOST_PASSWORD = ''  
PAYTM_STAGING_URL = 'https://securegw-stage.paytm.in'
PAYTM_PRODUCTION_URL = 'https://securegw.paytm.in'

HOSTNAME = '127.0.0.1:8000'

if DEBUG:
    PAYTM_URL = PAYTM_STAGING_URL
else:
    PAYTM_URL = PAYTM_PRODUCTION_URL

PAYTM_MERCHANT_KEY = 'vGLC!@e16pvBXN5O' # replace with original merchangt key
PAYTM_GATEWAY_SETTINGS = {
    'MID':'GUPDQo64705951932623', # replace with original merchangt id or MID
    'INDUSTRY_TYPE_ID':'Retail',
    'WEBSITE':'WEBSTAGING', # WEBSTAGING for websites -->> change this with production variables
    'CHANNEL_ID':'WEB', #WEB for websites
    'CALLBACK_URL':f'http://{HOSTNAME}/paytm/payment_response/', } # https:// if you are on production server

PAYTM_SAVE_SUCCESS_TRANSECTIONS_ONLY = True  # if this is true pa
