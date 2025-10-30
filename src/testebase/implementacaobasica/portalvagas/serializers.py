from .models import Vaga
from rest_framework import serializers


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = ['id', 'disciplina', 'curso', 'unidade', 'periodo']
        read_only_fields = ['id']