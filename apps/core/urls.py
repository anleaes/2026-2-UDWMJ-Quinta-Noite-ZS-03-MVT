
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('cadastro/sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
]
