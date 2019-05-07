from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()
router.register(r'users', views.UserView, basename='user')

urlpatterns = [
    # url(r'^user/login', views.LoginAuthTokenView.as_view()),  # drf自带的token认证模式（一般称为Session模式）
    # url(r'user/logout', views.LogoutAuthTokenView.as_view()),
    url(r'login', views.LoginJwtTokenView.as_view()),     # jwt的认证接口（较之drf自带的认证模式，占用的服务器端资源更少，安全性更高）
    url(r'logout', views.LogoutJwtTokenView.as_view()),
]

urlpatterns = urlpatterns + router.urls