from .models import Vagas
from rest_framework import serializers


class VagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vagas
        fields = ['id', 'disciplina', 'curso']
        read_only_fields = ['id']