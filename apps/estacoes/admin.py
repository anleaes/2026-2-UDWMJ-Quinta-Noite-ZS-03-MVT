from django.contrib import admin
from estacoes.models import EstacaoAtendimento


@admin.register(EstacaoAtendimento)
class EstacaoAtendimentoAdmin(admin.ModelAdmin):

    # Informações exibidas na listagem.
    list_display = (
        'identificacao',
        'numero_cadeira',
        'ambiente',
        'possui_lavatorio',
        'higienizada',
    )

    # Filtros disponíveis no painel.
    list_filter = (
        'ambiente',
        'possui_lavatorio',
        'higienizada',
    )

    # Campos utilizados na pesquisa.
    search_fields = (
        'identificacao',
        'ambiente',
    )

    # Ordenação dos registros.
    ordering = ('identificacao',)