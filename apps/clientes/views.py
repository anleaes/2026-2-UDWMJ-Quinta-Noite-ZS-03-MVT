from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente


def add_cliente(request):
    template_name = 'clientes/add_cliente.html'
    context = {}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('clientes:list_clientes')
    else:
        form = ClienteForm()
    context['form'] = form
    return render(request, template_name, context)


def list_clientes(request):
    template_name = 'clientes/list_clientes.html'
    clientes = Cliente.objects.select_related('pessoa').all()
    context = {
        'clientes': clientes
    }
    return render(request, template_name, context)


def edit_cliente(request, id_cliente):
    template_name = 'clientes/add_cliente.html'
    context = {}
    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:list_clientes')
    else:
        form = ClienteForm(instance=cliente)
    context['form'] = form
    return render(request, template_name, context)


def delete_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    cliente.delete()
    return redirect('clientes:list_clientes')