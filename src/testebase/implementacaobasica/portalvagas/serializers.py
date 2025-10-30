from .models import Vaga, Disciplina
from rest_framework import serializers


class DisciplinaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome']
        read_only_fields = ['id']

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = ['id', 'disciplina', 'unidade', 'periodo']
        read_only_fields = ['id']

