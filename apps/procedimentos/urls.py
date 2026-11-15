from django.urls import path
from . import views

app_name = 'procedimentos'

urlpatterns = [
    path('', views.list_procedimentos, name='list_procedimentos'),
    path('adicionar/', views.add_procedimento, name='add_procedimento'),
    path('editar/<int:id_procedimento>/', views.edit_procedimento, name='edit_procedimento'),
    path('excluir/<int:id_procedimento>/', views.delete_procedimento, name='delete_procedimento'),
]