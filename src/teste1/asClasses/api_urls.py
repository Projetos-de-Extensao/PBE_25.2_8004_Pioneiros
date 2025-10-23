from django.urls import path, include
from rest_framework import routers
from asClasses import api

router = routers.DefaultRouter()
router.register(r'alunos', api.AlunoViewSet)
router.register(r'candidatos', api.CandidatoViewSet)
router.register(r'alunos-monitorados', api.AlunoMonitoradoViewSet)
router.register(r'tas', api.TeachingAssistantViewSet)
router.register(r'professores', api.ProfessorViewSet)
router.register(r'casas', api.CASAViewSet)
router.register(r'disciplinas', api.DisciplinaViewSet)
router.register(r'inscricoes', api.InscricaoViewSet)
router.register(r'entrevistas', api.EntrevistaViewSet)
router.register(r'sessoes-monitoria', api.SessaoMonitoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]