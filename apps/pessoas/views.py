from django.shortcuts import render, redirect, get_object_or_404
from .forms import PessoaForm
from .models import Pessoa


def add_pessoa(request):
    template_name = 'pessoas/add_pessoa.html'
    context = {}
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('pessoas:list_pessoas')
    else:
        form = PessoaForm()
    context['form'] = form
    return render(request, template_name, context)


def list_pessoas(request):
    template_name = 'pessoas/list_pessoas.html'
    pessoas = Pessoa.objects.filter()
    context = {
        'pessoas': pessoas
    }
    return render(request, template_name, context)