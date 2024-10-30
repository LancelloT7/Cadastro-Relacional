from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'

class Cliente(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'

class Produto(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.produto}'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    item_pedido = models.ForeignKey(ItemPedido, on_delete=models.DO_NOTHING)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id} para {self.cliente}'
