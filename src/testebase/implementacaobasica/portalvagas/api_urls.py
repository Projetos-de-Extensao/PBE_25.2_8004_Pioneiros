from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import VagaViewSet

router = DefaultRouter()
router.register(r'vaga', VagaViewSet, basename='vaga')

urlpatterns = [
    path('', include(router.urls)),
]