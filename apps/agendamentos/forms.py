
from django import forms
from agendamentos.models import Agendamento


class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = Agendamento
        fields = [
            'cliente',
            'profissional',
            'estacao',
            'data_hora_inicio',
            'data_hora_fim',
            'status_agendamento',
            'confirmado_whatsapp',
            'observacoes_cliente',
        ]

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'profissional': forms.Select(attrs={'class': 'form-control'}),
            'estacao': forms.Select(attrs={'class': 'form-control'}),
            'data_hora_inicio': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            ),
            'data_hora_fim': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            ),
            'status_agendamento': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'confirmado_whatsapp': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
            'observacoes_cliente': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }

    # Garante que o horário de término seja posterior ao início.
    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('data_hora_inicio')
        fim = cleaned_data.get('data_hora_fim')

        if inicio and fim and fim <= inicio:
            self.add_error(
                'data_hora_fim',
                'O horário de término deve ser posterior ao início.'
            )

        return cleaned_data
