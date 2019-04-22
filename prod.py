from .settings import *

# 生产环境关闭DEBUG模式
DEBUG = False

# 生产环境开启跨域
CORS_ORIGIN_ALLOW_ALL = False

# 特别说明，下面这个不需要，因为前端是VueJS构建的，它默认使用static作为静态文件入口，我们nginx配置static为入口即可，保持一致，没Django什么事
STATIC_URL = '/static/'