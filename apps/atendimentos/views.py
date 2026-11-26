
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from atendimentos.forms import ItemAgendamentoForm
from atendimentos.models import ItemAgendamento


# Lista todos os itens de atendimento cadastrados.
def listar_atendimentos(request):
    atendimentos = ItemAgendamento.objects.select_related(
        'agendamento',
        'procedimento'
    ).all()

    return render(
        request,
        'atendimentos/listar.html',
        {'atendimentos': atendimentos}
    )


# Cadastra um novo item de atendimento.
def criar_atendimento(request):
    if request.method == 'POST':
        form = ItemAgendamentoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Item de atendimento cadastrado com sucesso!'
            )
            return redirect('atendimentos:listar_atendimentos')
    else:
        form = ItemAgendamentoForm()

    return render(
        request,
        'atendimentos/form.html',
        {'form': form}
    )


# Edita um item de atendimento existente.
def editar_atendimento(request, id):
    atendimento = get_object_or_404(ItemAgendamento, id=id)

    if request.method == 'POST':
        form = ItemAgendamentoForm(
            request.POST,
            request.FILES,
            instance=atendimento
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Item de atendimento atualizado com sucesso!'
            )
            return redirect('atendimentos:listar_atendimentos')
    else:
        form = ItemAgendamentoForm(instance=atendimento)

    return render(
        request,
        'atendimentos/form.html',
        {
            'form': form,
            'atendimento': atendimento
        }
    )


# Exclui um item de atendimento existente.
def excluir_atendimento(request, id):
    atendimento = get_object_or_404(ItemAgendamento, id=id)

    if request.method == 'POST':
        atendimento.delete()
        messages.success(
            request,
            'Item de atendimento excluído com sucesso!'
        )
        return redirect('atendimentos:listar_atendimentos')

    return render(
        request,
        'atendimentos/confirmar_exclusao.html',
        {'atendimento': atendimento}
    )
