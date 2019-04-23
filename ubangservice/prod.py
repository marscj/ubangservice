from .settings import *

# 生产环境关闭DEBUG模式
DEBUG = False

ALLOWED_HOSTS = ['ubangservice.com', '*']

# 生产环境开启跨域
CORS_ORIGIN_ALLOW_ALL = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'applogfile': {
        'level':'DEBUG',
        'class':'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(DJANGO_ROOT, 'ubangservice.log'),
        'maxBytes': 1024*1024*15, # 15MB
        'backupCount': 10,
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'ubangservice': {
            'handlers': ['applogfile',],
            'level': 'DEBUG',
        },
    }
}

# 特别说明，下面这个不需要，因为前端是VueJS构建的，它默认使用static作为静态文件入口，我们nginx配置static为入口即可，保持一致，没Django什么事
STATIC_URL = '/static/'