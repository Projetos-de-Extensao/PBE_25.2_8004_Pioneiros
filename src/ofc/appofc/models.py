from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(unique=True, max_length=100)


    def __str__(self):
        return self.nome

class UnidadeOpcoes(models.TextChoices):
    campus_barra = 'Barra'
    campus_centro = 'Centro'

class Vaga(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    unidade = models.CharField(max_length=20, choices=UnidadeOpcoes.choices, default=UnidadeOpcoes.campus_barra)

    def __str__(self):
        return self.disciplina.nome
    
    class Meta:
        unique_together = ('disciplina', 'unidade')
        
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')
    matricula = models.CharField(max_length=20, unique=True, verbose_name='Matrícula')
    curso = models.CharField(max_length=100)

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
    
