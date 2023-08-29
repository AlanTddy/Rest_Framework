from django.db import models
# Create your models here.

class Endereco(models.Model):
    estado = models.CharField(max_length=155)
    cidade = models.CharField(max_length=155)
    rua = models.CharField(max_length=155)
    numero = models.CharField(max_length=15)
    complemento = models.CharField(max_length=155)

    def __str__(self):
        return f'{self.id} | {self.estado}'

class Cliente(models.Model):
    nome = models.CharField(max_length=155)
    cpf = models.CharField(max_length=11)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, default=None, related_name="clientes")
    data_nasc = models.DateField()

    def __str__(self):
        return f'{self.id} | {self.nome}'

class Item (models.Model):
    codigo = models.IntegerField()
    nome = models.CharField()
    descricao = models.TextField()
    valor = models.FloatField()
    quantidade = models.FloatField()

    def __str__(self):
        return f'{self.id} | {self.nome}'

class Estoque (models.Model):
    produto = models.ForeignKey(Item, on_delete=models.CASCADE, default=None, related_name="estoque")

    def __str__(self):
        return f'{self.id} | {self.produto.nome}'