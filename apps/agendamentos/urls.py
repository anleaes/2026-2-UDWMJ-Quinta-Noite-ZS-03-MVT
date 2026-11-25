
from django.urls import path
from agendamentos import views

app_name = 'agendamentos'

urlpatterns = [
    path('listar/', views.listar_agendamentos, name='listar_agendamentos'),
    path('cadastrar/', views.criar_agendamento, name='criar_agendamento'),
    path('editar/<int:id>/', views.editar_agendamento, name='editar_agendamento'),
    path('excluir/<int:id>/', views.excluir_agendamento, name='excluir_agendamento'),
]
