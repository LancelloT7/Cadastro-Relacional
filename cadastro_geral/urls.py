from django.urls import path
from . import views


urlpatterns = [
    path('cadastro_funcionario/', views.cadastro_funcionario, name="cadastro_funcionario"),
    path('cadastro_cliente/', views.cadastro_cliente, name="cadastro_cliente,"),
    path('cadastro_produto/', views.cadastro_produto, name="cadastro_produto"),
    path('cadastro_pedido/', views.cadastro_pedido, name="cadastro_pedido"),
]
