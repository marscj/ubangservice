from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

SESSION_COOKIE_DOMAIN = 'localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}