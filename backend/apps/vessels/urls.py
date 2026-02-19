from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VesselViewSet

router = DefaultRouter()
router.register(r'', VesselViewSet, basename='vessels')

urlpatterns = [
    path('', include(router.urls)),
]
