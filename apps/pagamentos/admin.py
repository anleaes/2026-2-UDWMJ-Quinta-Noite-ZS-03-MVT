
from django.contrib import admin
from pagamentos.models import PagamentoSalao


# Registra o modelo PagamentoSalao no painel administrativo.
admin.site.register(PagamentoSalao)
