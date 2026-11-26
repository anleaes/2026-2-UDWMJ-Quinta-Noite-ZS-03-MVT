
from django.urls import path
from atendimentos import views

app_name = 'atendimentos'

urlpatterns = [
    path(
        'listar/',
        views.listar_atendimentos,
        name='listar_atendimentos'
    ),
    path(
        'cadastrar/',
        views.criar_atendimento,
        name='criar_atendimento'
    ),
    path(
        'editar/<int:id>/',
        views.editar_atendimento,
        name='editar_atendimento'
    ),
    path(
        'excluir/<int:id>/',
        views.excluir_atendimento,
        name='excluir_atendimento'
    ),
]
