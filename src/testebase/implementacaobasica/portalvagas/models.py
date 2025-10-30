from django.db import models

# Create your models here.
class Vaga(models.Model):
    disciplina = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    

    def __str__(self):
        return self.disciplina
    
    
# class Aluno

# class Professor(models.Model):
#     nome = models.CharField(max_length=100)
#     departamento = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome

# class TeachingAssistant(Candidato):
#     nome = models.CharField(max_length=100)
#     matricula = models.CharField(max_length=20)

#     def __str__(self):
#         return self.nome

# class Disciplina(models.Model):
#     nome = models.CharField(max_length=100)
#     curso = models.CharField(max_length=100)
#     professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
#     teaching_assistant = models.ForeignKey(TeachingAssistant, on_delete=models.CASCADE)
