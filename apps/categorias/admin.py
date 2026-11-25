from django.contrib import admin
from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'area_estetica', 'exige_biosseguranca', 'ativa')
    list_filter = ('ativa', 'exige_biosseguranca')
    search_fields = ('nome', 'descricao')