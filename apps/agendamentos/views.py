
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from agendamentos.forms import AgendamentoForm
from agendamentos.models import Agendamento


# Lista todos os agendamentos cadastrados.
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.select_related(
        'cliente', 'profissional', 'estacao'
    ).all()

    return render(
        request,
        'agendamentos/listar.html',
        {'agendamentos': agendamentos}
    )


# Cadastra um novo agendamento.
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento cadastrado com sucesso!')
            return redirect('agendamentos:listar_agendamentos')
    else:
        form = AgendamentoForm()

    return render(request, 'agendamentos/form.html', {'form': form})


# Edita um agendamento existente.
def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)

        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('agendamentos:listar_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)

    return render(
        request,
        'agendamentos/form.html',
        {'form': form, 'agendamento': agendamento}
    )


# Exclui um agendamento existente.
def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == 'POST':
        agendamento.delete()
        messages.success(request, 'Agendamento excluído com sucesso!')
        return redirect('agendamentos:listar_agendamentos')

    return render(
        request,
        'agendamentos/confirmar_exclusao.html',
        {'agendamento': agendamento}
    )
