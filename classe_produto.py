class Produto:
    def __init__(self, codproduto, nome, descricao, tamanho, preco):
        self.codproduto = codproduto
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco

    def desconto(self):
        preco_com_desconto = self.preco * 0.10
        pnovo = self.preco - preco_com_desconto
        return preco_com_desconto







