from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .import views 

router = DefaultRouter()
router.register(r'vehicles', views.VehicleView, basename='vehicles')
router.register(r'models', views.VehicleModelView, basename='models')

urlpatterns = router.urls