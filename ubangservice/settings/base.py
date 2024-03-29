from __future__ import absolute_import, unicode_literals

import os
import datetime

from django.utils.translation import gettext_lazy as _, pgettext_lazy
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))

FRONTEND_ROOT = 'frontend/dist'

SECRET_KEY = '&3dhis!j!lqdu6%d=og*mvuulew7tabjuph*b5_w5gyzy-6!uh'

# DEBUG = True

# ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field',
    'djmoney',
    'cacheops',
    
    'ubang.order',
    'ubang.booking',
    'ubang.job',
    'ubang.payment',
    'ubang.company',
    'ubang.user',
    'ubang.resource',
    'ubang.vehicle',
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
    
    'ubang.middleware.jwt_auth.JWTAuthenticationMiddleware',
    # 'ubang.middleware.create_by.WhoDidMiddleware',
    
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

REST_FRAMEWORK = {
    # 'TIME_FORMAT': '%H:%M',
    # 'TIME_INPUT_FORMATS': ('%H:%M',),
    # 'DATETIME_FORMAT': '%Y-%m-%d %H:%M',
    # 'DATETIME_INPUT_FORMATS': ('%Y-%m-%d %H:%M',),
    'ORDERING_PARAM': 'sort',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'ubang.middleware.rest_framework.CustomPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 2,
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    # 'PAGE_SIZE': 2,
    
}

ROOT_URLCONF = 'ubangservice.urls'

AUTH_USER_MODEL = 'user.CustomUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

USE_TZ = True

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
# CORS_ALLOW_HEADERS = ('*',)
# CORS_ALLOW_METHODS = ('*',)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    'Set-Cookie'
)

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

# 货币
DEFAULT_CURRENCY = 'AED'
DEFAULT_MAX_DIGITS = 10
DEFAULT_DECIMAL_PLACES = 2
CURRENCIES = ('AED', 'USD', 'CNY')
# CURRENCY_CHOICES = [('AED', 'AED €'), ('USD', 'USD $'), ('CNY', 'CNY ￥')]


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
DEFAULT_FULL_GUIDE_PRICE = Decimal(400.0)
DEFAULT_HALF_GUIDE_PRICE = Decimal(200.0)

# middleware create_by
CREATE_BY_FIELD = 'create_by'
UPDATE_BY_FIELD = 'update_by'
COMPANY_BY_FIELD = 'company_by'

# CELERY STUFF 
CELERY_BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379' 
CELERY_ACCEPT_CONTENT = ['application/json'] 
CELERY_TASK_SERIALIZER = 'json' 
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# cache
CACHEOPS_DEFAULTS = {
    'timeout': 60*60
}
CACHEOPS = {
    'auth.user': {'ops': 'get', 'timeout': 60*15},
    'auth.*': {'ops': ('fetch', 'get')},
    'auth.permission': {'ops': 'all'},
    '*.*': {},
}