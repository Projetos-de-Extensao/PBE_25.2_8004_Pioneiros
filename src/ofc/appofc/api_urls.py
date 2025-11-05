from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import VagaViewSet, DisciplinaViewSet, InscricaoViewSet

router = DefaultRouter()
router.register(r'vaga', VagaViewSet, basename='vaga')
router.register(r'disciplina', DisciplinaViewSet, basename='disciplina')
router.register(r'inscricao', InscricaoViewSet, basename='inscricao')



urlpatterns = [
    path('', include(router.urls)),
]
