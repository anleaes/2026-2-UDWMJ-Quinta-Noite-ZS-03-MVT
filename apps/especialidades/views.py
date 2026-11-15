from django.shortcuts import render, redirect, get_object_or_404
from .forms import EspecialidadeForm
from .models import Especialidade

def add_especialidade(request):
    template_name = 'especialidades/add_especialidade.html'
    context = {}
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('especialidades:list_especialidades')
    form = EspecialidadeForm()
    context['form'] = form
    return render(request, template_name, context)

def list_especialidades(request):
    template_name = 'especialidades/list_especialidades.html'
    especialidades = Especialidade.objects.filter()
    context = {
        'especialidades': especialidades
    }
    return render(request, template_name, context)

def edit_especialidade(request, id_especialidade):
    template_name = 'especialidades/add_especialidade.html'
    context = {}
    especialidade = get_object_or_404(Especialidade, id=id_especialidade)
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST, instance=especialidade)
        if form.is_valid():
            form.save()
            return redirect('especialidades:list_especialidades')
    form = EspecialidadeForm(instance=especialidade)
    context['form'] = form
    return render(request, template_name, context)

def delete_especialidade(request, id_especialidade):
    especialidade = Especialidade.objects.get(id=id_especialidade)
    especialidade.delete()
    return redirect('especialidades:list_especialidades')