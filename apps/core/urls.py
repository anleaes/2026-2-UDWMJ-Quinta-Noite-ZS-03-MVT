
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_not_required
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    # Tela de autenticação: permanece pública.
    path(
        'entrar/',
        login_not_required(
            auth_views.LoginView.as_view(
                template_name='registration/login.html'
            )
        ),
        name='login'
    ),

    # Encerra a sessão do usuário autenticado.
    path(
        'sair/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
