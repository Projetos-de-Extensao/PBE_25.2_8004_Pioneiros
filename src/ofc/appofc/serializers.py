from .models import Vaga, Disciplina, Aluno, Inscricao, Curso
from .analisador_historico import AnalisadorHistorico
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from drf_spectacular.utils import extend_schema_field


@extend_schema_field(serializers.CharField)
def get_creator_name(self, obj):
    return obj.creator.username

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nome', 'slug')

class DisciplinaSerializar(serializers.ModelSerializer):
    cursos = CursoSerializer(many=True, read_only=True)
    class Meta:
        model = Disciplina
        fields = ['id', 'nome','cursos']
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
        aluno = self.context['request'].user.aluno
        vaga_recebida = validated_data.get('vaga')

        if Inscricao.objects.filter(aluno=aluno, vaga=vaga_recebida).exists():
            raise serializers.ValidationError("Você já se inscreveu para esta vaga.")

        inscricao = Inscricao.objects.create(
            aluno=aluno,
            status='PENDENTE',
            **validated_data
        )

        # Tenta rodar o analisador automático
        try:
            caminho_pdf = inscricao.arquivo_historico.path
            analisador = AnalisadorHistorico(vaga_recebida=vaga_recebida)
            status_final = analisador.analisar_e_decidir(caminho_pdf)

            if status_final == "APROVADO":
                inscricao.status = "APROVADO"
                inscricao.save()

            if status_final == "REJEITADO":
                inscricao.status = "REJEITADO"
                inscricao.save()           
        except Exception as e:
             print(f"ERRO no analisador: {e}")

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
    # O frontend envia o 'slug' (ex: "computacao"), e este campo
    # automaticamente busca o objeto Curso correspondente no banco.
    curso = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Curso.objects.all()
    )

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
