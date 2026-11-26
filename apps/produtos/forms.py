from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome',
            'categoria',
            'marca',
            'descricao',
            'preco',
            'estoque',
            'ativo',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }