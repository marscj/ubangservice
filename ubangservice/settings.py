"""
Django settings for ubangservice project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

from django.utils.translation import gettext_lazy as _, pgettext_lazy
from decimal import Decimal

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_ROOT = 'frontend/dist'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3dhis!j!lqdu6%d=og*mvuulew7tabjuph*b5_w5gyzy-6!uh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'jet',
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    # 'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'django_countries',
    'phonenumber_field',
    'djmoney',
    'mptt',
    'inline_actions',
    
    'ubang.order',
    'ubang.booking',
    'ubang.payment',
    'ubang.company',
    'ubang.task',
    'ubang.user',
    'ubang.resource',
    'ubang.vehicle',
    'ubang.itinerary'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'ubang.middleware.create_by.WhoDidMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}

ROOT_URLCONF = 'ubangservice.urls'

AUTH_USER_MODEL = 'user.CustomUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'static')],
        'DIRS': [FRONTEND_ROOT, os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ubangservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Dubai'

USE_I18N = True

USE_L10N = False

# USE_TZ = True
USE_TZ = False

TIME_INPUT_FORMATS = [
    '%H:%M'
]

DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M'
]

DATETIME_FORMAT = 'Y-m-d H:i'

DATE_FORMAT = 'Y-m-d'

SHORT_DATE_FORMAT = 'Y-m-d'

SHORT_DATETIME_FORMAT =  'Y-m-d H:i'

# 跨域
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ('*',)
CORS_ALLOW_HEADERS = ('*',)
CORS_ALLOW_METHODS = ('*',)

# 静态资源
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, FRONTEND_ROOT),
    os.path.join(BASE_DIR, FRONTEND_ROOT + '/static'),
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

# Grappelli admin interface
GRAPPELLI_ADMIN_TITLE = 'UBang'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
GRAPPELLI_SWITCH_USER = True
GRAPPELLI_CLEAN_INPUT_TYPES = True

# 货币
DEFAULT_CURRENCY = 'AED'
DEFAULT_MAX_DIGITS = 10
DEFAULT_DECIMAL_PLACES = 2
# CURRENCIES = ('AED', 'USD', 'CNY')
CURRENCY_CHOICES = [('AED', 'AED €'), ('USD', 'USD $'), ('CNY', 'CNY ￥')]


# 支付
DUMMY = 'dummy'
STRIPE = 'stripe'
CASH = 'cash'
TRANSFER = 'Transfer'

CHECKOUT_PAYMENT_GATEWAYS = {
    DUMMY: pgettext_lazy('Payment method name', 'Dummy gateway')}

PAYMENT_GATEWAYS = {
    DUMMY: {
        'module': 'saleor.payment.gateways.dummy',
        'connection_params': {}
    },
    CASH: {

    },
    TRANSFER: {
        
    }
    # STRIPE: {
    #     'module': 'saleor.payment.gateways.stripe',
    #     'connection_params': {
    #         'public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
    #         'secret_key': os.environ.get('STRIPE_SECRET_KEY'),
    #         'store_name': os.environ.get(
    #             'STRIPE_STORE_NAME', 'Saleor'),
    #         'store_image': os.environ.get('STRIPE_STORE_IMAGE', None),
    #         'prefill': get_bool_from_env('STRIPE_PREFILL', True),
    #         'remember_me': os.environ.get('STRIPE_REMEMBER_ME', True),
    #         'locale': os.environ.get('STRIPE_LOCALE', 'auto'),
    #         'enable_billing_address': os.environ.get(
    #             'STRIPE_ENABLE_BILLING_ADDRESS', False),
    #         'enable_shipping_address': os.environ.get(
    #             'STRIPE_ENABLE_SHIPPING_ADDRESS', False)
    #     }
    # }
}

# 导游费用
DEFAULT_GUIDE_PRICE = Decimal(400.0)

# middleware create_by
CREATE_BY_FIELD = 'create_by'
UPDATE_BY_FIELD = 'update_by'
COMPANY_BY_FIELD = 'company_by'

# redis
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

# mptt
MPTT_ADMIN_LEVEL_INDENT = 30

# jwt
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_COOKIE': 'jwt_auth_token',
}