from django.db import models

# Create your models here.
class Produto:
    def __init__(self, nome, descricao, quantidade,preco):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco


