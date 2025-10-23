from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
        data_criacao = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Pedido #{self.id} - {self.data_criacao.strftime('%Y-%m-%d %H:%M:%S')}"

class TA(models.Model):
        aluno = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
        disciplina = models.ForeignKey(Produto, on_delete=models.CASCADE)
        quantidade = models.PositiveIntegerField(default=1)

        def __str__(self):
            return f"{self.quantidade} x {self.produto.nome} (Pedido #{self.pedido.id})"