from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'marca', 'preco', 'estoque', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome', 'marca')