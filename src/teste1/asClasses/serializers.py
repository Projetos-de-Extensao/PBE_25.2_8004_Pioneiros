from rest_framework import serializers
from . import models

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = ['id', 'matricula', 'nome', 'email']

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidato
        fields = ['id', 'matricula', 'nome', 'email', 'status']

class AlunoMonitoradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlunoMonitorado
        fields = ['id', 'matricula', 'nome', 'email', 'aulas_participadas']

class TeachingAssistantSerializer(serializers.ModelSerializer):
    disciplinas = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Disciplina.objects.all(), required=False)
    supervisor = serializers.PrimaryKeyRelatedField(queryset=models.Professor.objects.all(), allow_null=True, required=False)
    acompanhada_por = serializers.PrimaryKeyRelatedField(queryset=models.CASA.objects.all(), allow_null=True, required=False)

    class Meta:
        model = models.TeachingAssistant
        fields = ['id', 'matricula', 'nome', 'email', 'disciplinas', 'supervisor', 'acompanhada_por']

class ProfessorSerializer(serializers.ModelSerializer):
    supervisionados = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Professor
        fields = ['id', 'nome', 'email', 'senha', 'supervisionados']
        extra_kwargs = {'senha': {'write_only': True}}

class CASASerializer(serializers.ModelSerializer):
    entrevistas_agendadas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tas_acompanhadas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.CASA
        fields = ['id', 'nome', 'email', 'entrevistas_agendadas', 'tas_acompanhadas']

class DisciplinaSerializer(serializers.ModelSerializer):
    monitor = serializers.PrimaryKeyRelatedField(queryset=models.TeachingAssistant.objects.all(), allow_null=True, required=False)

    class Meta:
        model = models.Disciplina
        fields = ['id', 'nome', 'area', 'monitor']

class InscricaoSerializer(serializers.ModelSerializer):
    alunos = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Candidato.objects.all(), required=False)
    entrevista = serializers.PrimaryKeyRelatedField(queryset=models.Entrevista.objects.all(), allow_null=True, required=False)

    class Meta:
        model = models.Inscricao
        fields = ['id', 'disciplina', 'alunos', 'entrevista']

    def create(self, validated_data):
        alunos = validated_data.pop('alunos', [])
        inscricao = models.Inscricao.objects.create(**validated_data)
        if alunos:
            inscricao.alunos.set(alunos)
        return inscricao

    def update(self, instance, validated_data):
        alunos = validated_data.pop('alunos', None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        if alunos is not None:
            instance.alunos.set(alunos)
        return instance

class EntrevistaSerializer(serializers.ModelSerializer):
    candidatos = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Candidato.objects.all())
    professores = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Professor.objects.all())
    agendada_por = serializers.PrimaryKeyRelatedField(queryset=models.CASA.objects.all(), allow_null=True, required=False)

    class Meta:
        model = models.Entrevista
        fields = ['id', 'candidatos', 'professores', 'agendada_por', 'data']

    def create(self, validated_data):
        candidatos = validated_data.pop('candidatos', [])
        professores = validated_data.pop('professores', [])
        entrevista = models.Entrevista.objects.create(**validated_data)
        entrevista.candidatos.set(candidatos)
        entrevista.professores.set(professores)
        return entrevista

class SessaoMonitoriaSerializer(serializers.ModelSerializer):
    monitorados = serializers.PrimaryKeyRelatedField(many=True, queryset=models.AlunoMonitorado.objects.all(), required=False)

    class Meta:
        model = models.SessaoMonitoria
        fields = ['id', 'data', 'disciplina', 'monitorados']

    def create(self, validated_data):
        monitorados = validated_data.pop('monitorados', [])
        sessao = models.SessaoMonitoria.objects.create(**validated_data)
        if monitorados:
            sessao.monitorados.set(monitorados)
        return sessao

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['qtd_alunos'] = instance.qtd_alunos
        return rep