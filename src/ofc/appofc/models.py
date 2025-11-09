from django.db import models
from django.contrib.auth.models import User

# adm - "Administração"
# arquitetura - "Arquitetura e Urbanismo"
# ciencias_economicas - "Ciências Econômicas"
# publicidade - "Comunicação Social – Publicidade e Propaganda"
# direito - "Direito"
# engcivil - "Engenharia Civil"
# engproducao - "Engenharia de Produção"
# engmecanica - "Engenharia Mecânica"
# jornalismo - "Jornalismo"
# relacoes_internacionais - "Relações Internacionais"
# ciencia_dados - "Ciência de Dados"
# engsoftware - "Engenharia de Software"
# engcomputacao - "Engenharia da Computação"

class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=60)
    curso = models.ManyToManyField(Curso, related_name='disciplinas')

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    class UnidadeOpcoes(models.TextChoices):
        campus_barra = 'Barra'
        campus_centro = 'Centro'

    unidade = models.CharField(max_length=20, choices=UnidadeOpcoes.choices, default=UnidadeOpcoes.campus_barra)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)


    def __str__(self):
        return self.disciplina.nome
    
    class Meta:
        unique_together = ('disciplina', 'unidade')



class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')
    matricula = models.CharField(max_length=20, unique=True, verbose_name='Matrícula')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return f'{self.matricula} - {self.user.get_full_name()}'

class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    arquivo_historico = models.FileField(upload_to='historicos/')
    status_choices = [
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('REJEITADO', 'Rejeitado'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='PENDENTE')
    class Meta:
        unique_together = ('vaga', 'aluno')
    
    def __str__(self):
        return f'{self.aluno} - {self.vaga}'
    
