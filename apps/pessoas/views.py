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

def edit_pessoa(request, id_pessoa):
    template_name = 'pessoas/add_pessoas.html'
    context = {}
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoas:list_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    context['form'] = form
    return render(request, template_name, context)


def delete_pessoa(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    pessoa.delete()
    return redirect('pessoas:list_pessoas')