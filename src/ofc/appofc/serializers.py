from .models import Vaga, Disciplina, Aluno, Inscricao
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction



class DisciplinaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome']
        read_only_fields = ['id']

class VagaSerializer(serializers.ModelSerializer):
    disciplina = DisciplinaSerializar(read_only=True)
    
    class Meta:
        model = Vaga
        fields = ['id', 'disciplina', 'unidade']
        read_only_fields = ['id']

# pra post
class InscricaoCreateSerializer(serializers.ModelSerializer):
    vaga = serializers.PrimaryKeyRelatedField(queryset=Vaga.objects.all())

    class Meta:
        model = Inscricao
        fields = ('vaga', 'arquivo_historico') 
        
    def create(self, validated_data):
        try:
            aluno = self.context['request'].user.aluno
        except AttributeError:
            raise serializers.ValidationError("O usuário logado não é um aluno.")

        
        vaga = validated_data.get('vaga')
        if Inscricao.objects.filter(aluno=aluno, vaga=vaga).exists():
            raise serializers.ValidationError("Você já se inscreveu para esta vaga.")
        
        inscricao = Inscricao.objects.create(
            aluno=aluno,
            **validated_data
        )
        return inscricao

# pra get
class InscricaoSerializer(serializers.ModelSerializer):
    vaga = VagaSerializer(read_only=True)
    nome_aluno = serializers.CharField(source='aluno.user.get_full_name', read_only=True)
    
    class Meta:
        model = Inscricao
        fields = ['id', 'vaga', 'arquivo_historico', 'nome_aluno', 'status']
        read_only_fields = ['id']

# pra get
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('matricula', 'curso')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

# pra post
class CadastroAlunoSerializer(serializers.ModelSerializer):
    aluno = AlunoSerializer()
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'aluno')

    @transaction.atomic
    def create(self, validated_data):
        aluno_data = validated_data.pop('aluno')
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        

        try:
            matricula_para_username = aluno_data['matricula']
        except KeyError:
            raise serializers.ValidationError({"aluno": "Matrícula é obrigatória."})

        user = User.objects.create_user(
            username=matricula_para_username,    
            password=password,
            email=email,
            **validated_data   
        )
        
        Aluno.objects.create(
            user=user,
            **aluno_data
        )
        return user
