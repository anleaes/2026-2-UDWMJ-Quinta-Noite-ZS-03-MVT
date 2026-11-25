
from django.shortcuts import render, redirect, get_object_or_404
from pagamentos.models import PagamentoSalao
from pagamentos.forms import PagamentoSalaoForm


# Lista todos os pagamentos cadastrados.
def listar_pagamentos(request):
    pagamentos = PagamentoSalao.objects.select_related(
        'agendamento'
    ).all()

    return render(
        request,
        'pagamentos/listar_pagamentos.html',
        {'pagamentos': pagamentos}
    )


# Cadastra um novo pagamento.
def criar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoSalaoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('pagamentos:listar_pagamentos')
    else:
        form = PagamentoSalaoForm()

    return render(
        request,
        'pagamentos/form_pagamento.html',
        {
            'form': form,
            'titulo': 'Cadastrar Pagamento',
        }
    )


# Edita um pagamento existente.
def editar_pagamento(request, id):
    pagamento = get_object_or_404(PagamentoSalao, pk=id)

    if request.method == 'POST':
        form = PagamentoSalaoForm(
            request.POST,
            request.FILES,
            instance=pagamento
        )

        if form.is_valid():
            form.save()
            return redirect('pagamentos:listar_pagamentos')
    else:
        form = PagamentoSalaoForm(instance=pagamento)

    return render(
        request,
        'pagamentos/form_pagamento.html',
        {
            'form': form,
            'titulo': 'Editar Pagamento',
        }
    )


# Exclui um pagamento após confirmação.
def excluir_pagamento(request, id):
    pagamento = get_object_or_404(PagamentoSalao, pk=id)

    if request.method == 'POST':
        pagamento.delete()
        return redirect('pagamentos:listar_pagamentos')

    return render(
        request,
        'pagamentos/confirmar_exclusao.html',
        {'pagamento': pagamento}
    )
