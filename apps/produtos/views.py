from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto


def add_produto(request):
    template_name = 'produtos/add_produto.html'
    context = {}
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('produtos:list_produtos')
    else:
        form = ProdutoForm()
    context['form'] = form
    return render(request, template_name, context)


def list_produtos(request):
    template_name = 'produtos/list_produtos.html'
    produtos = Produto.objects.select_related('categoria').all()
    context = {
        'produtos': produtos
    }
    return render(request, template_name, context)


def edit_produto(request, id_produto):
    template_name = 'produtos/add_produto.html'
    context = {}
    produto = get_object_or_404(Produto, id=id_produto)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:list_produtos')
    else:
        form = ProdutoForm(instance=produto)
    context['form'] = form
    return render(request, template_name, context)


def delete_produto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto)
    produto.delete()
    return redirect('produtos:list_produtos')