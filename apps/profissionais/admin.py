from django.contrib import admin
from .models import Profissional


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'especialidade', 'ativo')
    list_filter = ('ativo',)