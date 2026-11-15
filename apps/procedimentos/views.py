from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProcedimentoForm
from .models import Procedimento

def add_procedimento(request):
    template_name = 'procedimentos/add_procedimento.html'
    context = {}
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('procedimentos:list_procedimentos')
    form = ProcedimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_procedimentos(request):
    template_name = 'procedimentos/list_procedimentos.html'
    procedimentos = Procedimento.objects.select_related('especialidade').all()
    context = {
        'procedimentos': procedimentos
    }
    return render(request, template_name, context)

def edit_procedimento(request, id_procedimento):
    template_name = 'procedimentos/add_procedimento.html'
    context = {}
    procedimento = get_object_or_404(Procedimento, id=id_procedimento)
    if request.method == 'POST':
        form = ProcedimentoForm(request.POST, request.FILES, instance=procedimento)
        if form.is_valid():
            form.save()
            return redirect('procedimentos:list_procedimentos')
    form = ProcedimentoForm(instance=procedimento)
    context['form'] = form
    return render(request, template_name, context)

def delete_procedimento(request, id_procedimento):
    procedimento = Procedimento.objects.get(id=id_procedimento)
    procedimento.delete()
    return redirect('procedimentos:list_procedimentos')