
from django.shortcuts import render, redirect
from .forms import CadastroUsuarioForm


def home(request):
    return render(request, 'core/home.html', {})


def cadastro_usuario(request):
    # Processa o formulário enviado pelo usuário.
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('core:cadastro_sucesso')
    else:
        form = CadastroUsuarioForm()

    return render(request, 'core/cadastro.html', {'form': form})


def cadastro_sucesso(request):
    return render(request, 'core/cadastro_sucesso.html')
