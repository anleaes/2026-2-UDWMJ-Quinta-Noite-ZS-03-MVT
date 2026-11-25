
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Exige autenticação para acessar a página inicial.
@login_required
def home(request):
    return render(request, 'core/home.html', {})
