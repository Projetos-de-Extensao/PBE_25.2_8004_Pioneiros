from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Vaga, Disciplina, Aluno
from .serializers import VagaSerializer, DisciplinaSerializar
from rest_framework.permissions import IsAuthenticated


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializar
    permission_classes = [IsAuthenticated]

class VagaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vaga.objects.all() 
    serializer_class = VagaSerializer 
    permission_classes = [IsAuthenticated]
