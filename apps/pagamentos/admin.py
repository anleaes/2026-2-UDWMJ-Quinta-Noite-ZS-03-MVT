from django.contrib import admin
from pagamentos.models import PagamentoSalao


@admin.register(PagamentoSalao)
class PagamentoSalaoAdmin(admin.ModelAdmin):

    # Informações exibidas na listagem do painel administrativo.
    list_display = (
        'id',
        'agendamento',
        'valor_total_servicos',
        'gorjeta_profissional',
        'forma_pagamento',
        'pago',
        'data_pagamento',
    )

    # Filtros para localizar pagamentos.
    list_filter = (
        'forma_pagamento',
        'pago',
        'data_pagamento',
    )

    # Campos utilizados pela pesquisa.
    search_fields = (
        'agendamento__id',
    )

    # Permite alterar o status de pagamento diretamente na listagem.
    list_editable = (
        'pago',
    )

    # Ordenação padrão: pagamentos mais recentes primeiro.
    ordering = ('-data_pagamento',)
