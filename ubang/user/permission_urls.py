from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .import views

urlpatterns =[
    url(r'permissions', views.PermissionView.as_view(), name='permissions'),
]