from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Produto

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco')
        produto = Produto( nome, descricao,quantidade,preco)
        return HttpResponse(
            f"Cliente cadastrado com sucesso! <br> "
            f"Nome: {produto.nome}"
            f"<br> descricao: {produto.descricao}"
            f"<br>Quantiadade: {produto.quantidade}"
            f"<br>Preco: {produto.preco}"
        )
    return render(request, 'cadastro_produto.html')