from django.contrib import admin
from atendimentos.models import ItemAgendamento


@admin.register(ItemAgendamento)
class ItemAgendamentoAdmin(admin.ModelAdmin):

    # Informações exibidas na listagem do painel administrativo.
    list_display = (
        'id',
        'agendamento',
        'procedimento',
        'valor_cobrado',
        'desconto_aplicado',
        'tempo_real_minutos',
    )

    # Filtros disponíveis para facilitar a consulta dos registros.
    list_filter = (
        'procedimento',
    )

    # Campos utilizados pela pesquisa do painel.
    search_fields = (
        'agendamento__id',
        'procedimento__nome',
        'quimica_utilizada',
    )

    # Ordenação padrão dos registros.
    ordering = ('id',)