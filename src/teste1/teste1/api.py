from rest_framework import viewsets, permissions
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models, serializers

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = models.Aluno.objects.all()
    serializer_class = serializers.AlunoSerializer
    permission_classes = [permissions.AllowAny]

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = models.Candidato.objects.all()
    serializer_class = serializers.CandidatoSerializer
    permission_classes = [permissions.AllowAny]

class AlunoMonitoradoViewSet(viewsets.ModelViewSet):
    queryset = models.AlunoMonitorado.objects.all()
    serializer_class = serializers.AlunoMonitoradoSerializer
    permission_classes = [permissions.AllowAny]

class TeachingAssistantViewSet(viewsets.ModelViewSet):
    queryset = models.TeachingAssistant.objects.all()
    serializer_class = serializers.TeachingAssistantSerializer
    permission_classes = [permissions.AllowAny]

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = models.Professor.objects.all()
    serializer_class = serializers.ProfessorSerializer
    permission_classes = [permissions.AllowAny]

class CASAViewSet(viewsets.ModelViewSet):
    queryset = models.CASA.objects.all()
    serializer_class = serializers.CASASerializer
    permission_classes = [permissions.AllowAny]

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = models.Disciplina.objects.all()
    serializer_class = serializers.DisciplinaSerializer
    permission_classes = [permissions.AllowAny]

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = models.Inscricao.objects.all()
    serializer_class = serializers.InscricaoSerializer
    permission_classes = [permissions.AllowAny]

class EntrevistaViewSet(viewsets.ModelViewSet):
    queryset = models.Entrevista.objects.all()
    serializer_class = serializers.EntrevistaSerializer
    permission_classes = [permissions.AllowAny]

class SessaoMonitoriaViewSet(viewsets.ModelViewSet):
    queryset = models.SessaoMonitoria.objects.all()
    serializer_class = serializers.SessaoMonitoriaSerializer
    permission_classes = [permissions.AllowAny]