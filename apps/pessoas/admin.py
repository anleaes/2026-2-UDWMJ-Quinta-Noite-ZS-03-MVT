from django.contrib import admin
from .models import Pessoa

# Register your models here.
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'telefone', 'email', 'ativo')
    search_fields = ('nome', 'cpf', 'email')
    list_filter = ('ativo',)