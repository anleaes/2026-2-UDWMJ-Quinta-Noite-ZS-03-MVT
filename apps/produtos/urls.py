from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.list_produtos, name='list_produtos'),
    path('adicionar/', views.add_produto, name='add_produto'),
    path('editar/<int:id_produto>/', views.edit_produto, name='edit_produto'),
    path('excluir/<int:id_produto>/', views.delete_produto, name='delete_produto'),
]