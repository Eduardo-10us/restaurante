from django.shortcuts import render

from categoria.models import Categoria
from produto.models import Produto


# Create your views here.

def inicio(request):
    return render(request, 'home.html')

def historia(request):
    return render(request,'historia.html')

def administrativo(request):
    return render(request, 'menuadm.html')

def sushi(request):
    sushi = Categoria.objects.get(nome='sushi')
    produtos = Produto.objects.filter(categoria=sushi)
    return render(request,"sushi.html",{'produtos':produtos})

def sashimi(request):
    sashimi = Categoria.objects.get(nome='sashimi')
    produtos = Produto.objects.filter(categoria=sashimi)
    return render(request,"sashimi.html",{'produtos':produtos})

def temaki(request):
    temaki = Categoria.objects.get(nome='temaki')
    produtos = Produto.objects.filter(categoria=temaki)
    return render(request,"temaki.html",{'produtos':produtos})

def diversos(request):
    diversos = Categoria.objects.get(nome='diversos')
    produtos = Produto.objects.filter(categoria=diversos)
    return render(request,"diversos.html",{'produtos':produtos})

def sobremesas(request):
    sobremesas = Categoria.objects.get(nome='sobremesas')
    produtos = Produto.objects.filter(categoria=sobremesas)
    return render(request,"sobremesas.html",{'produtos':produtos})

def bebidas(request):
    bebidas = Categoria.objects.get(nome='bebidas')
    produtos = Produto.objects.filter(categoria=bebidas)
    return render(request,"bebidas.html",{'produtos':produtos})

def contatos(request):
    return render(request, 'contatos.html')

def menucli(request):
    return render(request, 'menucliente.html')

def home(request):
    return render(request, 'home.html')


