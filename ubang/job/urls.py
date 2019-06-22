from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .import views 

router = DefaultRouter()
router.register(r'jobs', views.JobViewSet, basename='job')

urlpatterns = router.urls