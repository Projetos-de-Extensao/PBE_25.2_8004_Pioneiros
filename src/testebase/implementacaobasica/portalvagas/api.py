from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Vaga, Disciplina
from .serializers import VagaSerializer, DisciplinaSerializar

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializar


class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
