
from django import forms
from pagamentos.models import PagamentoSalao


class PagamentoSalaoForm(forms.ModelForm):

    class Meta:
        model = PagamentoSalao

        # Campos disponíveis no formulário de pagamento.
        fields = [
            'agendamento',
            'valor_total_servicos',
            'gorjeta_profissional',
            'forma_pagamento',
            'pago',
            'comprovante_pix_pdf',
        ]

        # Personalização dos campos para utilizar o Bootstrap.
        widgets = {
            'agendamento': forms.Select(attrs={
                'class': 'form-select',
            }),
            'valor_total_servicos': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
            }),
            'gorjeta_profissional': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
            }),
            'forma_pagamento': forms.Select(attrs={
                'class': 'form-select',
            }),
            'pago': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'comprovante_pix_pdf': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
