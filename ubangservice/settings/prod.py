from .base import *

DEBUG = False

ADMINS = (
    ('Mars', 'mjx_cj@gmail.com'),
)

ALLOWED_HOSTS = ['ubangservice.com', '*']

SESSION_COOKIE_DOMAIN = 'ubangservice.com'

CORS_ORIGIN_ALLOW_ALL = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_AUTH_COOKIE': 'jwt_auth_token',
    'JWT_GET_USER_SECRET_KEY': 'ubang.user.models.jwt_get_secret_key'
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename':  os.path.join(BASE_DIR, 'debug.log'),
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }