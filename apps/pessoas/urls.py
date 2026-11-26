from django.urls import path
from . import views

app_name = 'pessoas'

urlpatterns = [
    path('', views.list_pessoas, name='list_pessoas'),
    path('adicionar/', views.add_pessoa, name='add_pessoa'),
    path('editar/<int:id_pessoa>/', views.edit_pessoa, name='edit_pessoa'),
    path('excluir/<int:id_pessoa>/', views.delete_pessoa, name='delete_pessoa'),
]