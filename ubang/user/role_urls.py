from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .import views 

router = DefaultRouter()
router.register(r'roles', views.RoleView, basename='roles')

urlpatterns = router.urls