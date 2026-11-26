
from django import forms
from atendimentos.models import ItemAgendamento


class ItemAgendamentoForm(forms.ModelForm):

    class Meta:
        model = ItemAgendamento
        fields = [
            'agendamento',
            'procedimento',
            'valor_cobrado',
            'desconto_aplicado',
            'tempo_real_minutos',
            'quimica_utilizada',
            'foto_antes_depois',
        ]

        widgets = {
            'agendamento': forms.Select(attrs={
                'class': 'form-control'
            }),
            'procedimento': forms.Select(attrs={
                'class': 'form-control'
            }),
            'valor_cobrado': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'desconto_aplicado': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'tempo_real_minutos': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'quimica_utilizada': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'foto_antes_depois': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    # Impede que o desconto ultrapasse o valor cobrado.
    def clean(self):
        cleaned_data = super().clean()

        valor = cleaned_data.get('valor_cobrado')
        desconto = cleaned_data.get('desconto_aplicado')

        if valor is not None and desconto is not None:
            if desconto > valor:
                self.add_error(
                    'desconto_aplicado',
                    'O desconto não pode ser maior que o valor cobrado.'
                )

        return cleaned_data
