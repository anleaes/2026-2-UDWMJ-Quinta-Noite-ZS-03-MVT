
from django.shortcuts import render, redirect, get_object_or_404

from avaliacoes.models import EstacaoAtendimento
from avaliacoes.forms import EstacaoAtendimentoForm


# Lista todas as estações cadastradas.
def listar_estacoes(request):
    estacoes = EstacaoAtendimento.objects.all()

    return render(
        request,
        'avaliacoes/listar_estacoes.html',
        {'estacoes': estacoes}
    )


# Cadastra uma nova estação.
def criar_estacao(request):
    if request.method == 'POST':
        form = EstacaoAtendimentoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('avaliacoes:listar_estacoes')

    else:
        form = EstacaoAtendimentoForm()

    return render(
        request,
        'avaliacoes/form_estacao.html',
        {'form': form, 'titulo': 'Cadastrar Estação'}
    )


# Edita uma estação já cadastrada.
def editar_estacao(request, id):
    estacao = get_object_or_404(EstacaoAtendimento, pk=id)

    if request.method == 'POST':
        form = EstacaoAtendimentoForm(
            request.POST,
            request.FILES,
            instance=estacao
        )

        if form.is_valid():
            form.save()
            return redirect('avaliacoes:listar_estacoes')

    else:
        form = EstacaoAtendimentoForm(instance=estacao)

    return render(
        request,
        'avaliacoes/form_estacao.html',
        {'form': form, 'titulo': 'Editar Estação'}
    )


# Exclui uma estação após confirmação.
def excluir_estacao(request, id):
    estacao = get_object_or_404(EstacaoAtendimento, pk=id)

    if request.method == 'POST':
        estacao.delete()
        return redirect('avaliacoes:listar_estacoes')

    return render(
        request,
        'avaliacoes/confirmar_exclusao.html',
        {'estacao': estacao}
    )
