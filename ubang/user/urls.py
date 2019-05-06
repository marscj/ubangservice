
from django.conf.urls import url, include

from .import views

urlpatterns = [
    # url(r'^user/login', views.LoginAuthTokenView.as_view()),  # drf自带的token认证模式（一般称为Session模式）
    # url(r'user/logout', views.LogoutAuthTokenView.as_view()),
    url(r'user/login', views.LoginJwtTokenView.as_view()),     # jwt的认证接口（较之drf自带的认证模式，占用的服务器端资源更少，安全性更高）
    url(r'user/logout', views.LogoutJwtTokenView.as_view()),

    url(r'user/info', views.UserInfo.as_view()),
]
