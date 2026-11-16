
from django.contrib import admin
from agendamentos.models import Agendamento


# Registra o modelo Agendamento no painel administrativo.
admin.site.register(Agendamento)
