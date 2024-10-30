from django.shortcuts import render
from .models import Funcionario, Cliente, Pedido, Produto, ItemPedido
from django.http import HttpResponse

# Create your views here.


def cadastro_funcionario(request):
    if request.method == "GET":
        return render(request, 'funcionario.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')

        funcionario = Funcionario(nome=nome)
        funcionario.save()


def cadastro_cliente(request):
    if request.method == "GET":
        return render(request, 'cliente.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')

        cliente = Cliente(nome=nome)
        cliente.save()


def cadastro_produto(request):
    if request.method == "GET":
        return render(request, 'produto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')

        produto = Produto(nome=nome)
        produto.save()

def cadastro_pedido(request):
    produtos = Produto.objects.all()
    funcionarios = Funcionario.objects.all()
    clientes = Cliente.objects.all()
    
    return HttpResponse('pedido')



