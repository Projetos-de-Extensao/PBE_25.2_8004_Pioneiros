from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VagaViewSet, DisciplinaViewSet, InscricaoViewSet, CursoViewSet

router = DefaultRouter()
router.register(r'vaga', VagaViewSet, basename='vaga')
router.register(r'disciplina', DisciplinaViewSet, basename='disciplina')
router.register(r'inscricao', InscricaoViewSet, basename='inscricao')
router.register(r'curso', CursoViewSet, basename='curso')



urlpatterns = [
    path('', include(router.urls)),
]
