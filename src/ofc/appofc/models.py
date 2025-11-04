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