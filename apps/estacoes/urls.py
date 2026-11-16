
from django.urls import path
from estacoes import views

# Namespace do aplicativo de estações.
app_name = 'estacoes'

urlpatterns = [
    # Lista todas as estações.
    path('listar/', views.listar_estacoes, name='listar_estacoes'),

    # Cadastra uma nova estação.
    path('cadastrar/', views.criar_estacao, name='criar_estacao'),

    # Edita uma estação existente.
    path('editar/<int:id>/', views.editar_estacao, name='editar_estacao'),

    # Exclui uma estação.
    path('excluir/<int:id>/', views.excluir_estacao, name='excluir_estacao'),
]
