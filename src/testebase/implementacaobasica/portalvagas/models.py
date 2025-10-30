from django.db import models

# Create your models here.
class Vaga(models.Model):
    disciplina = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.disciplina
    
class Candidato