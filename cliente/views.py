from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .models import Cliente

from django.shortcuts import render, redirect
from .models import Cliente
import requests

def busca_cep(request):
    endereco = {}

    if request.method == 'POST':
        cep = request.POST.get('cep')
        url = f"HTTps://https://viacep.com.br/ws/{cep}/json/"

        






def cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')

        if nome and telefone and email and cep and numero and complemento:
            cliente = Cliente(
                nome=nome,
                telefone=telefone,
                email=email,
                cep=cep,
                numero=numero,
                complemento=complemento
            )
            cliente.save()
            return redirect('cadastro_cliente')

    return render(request, 'cadastro_cliente.html')


