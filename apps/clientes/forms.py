from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'pessoa',
            'preferencias',
            'pontos_fidelidade',
            'ativo',
        ]
        widgets = {
            'preferencias': forms.Textarea(attrs={'rows': 3}),
        }