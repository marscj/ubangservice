import os
from .settings import *

# 生产环境关闭DEBUG模式
DEBUG = False

ALLOWED_HOSTS = ['ubangservice.com', '*']

# 生产环境开启跨域
CORS_ORIGIN_ALLOW_ALL = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename':  os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# 特别说明，下面这个不需要，因为前端是VueJS构建的，它默认使用static作为静态文件入口，我们nginx配置static为入口即可，保持一致，没Django什么事
STATIC_URL = '/static/'