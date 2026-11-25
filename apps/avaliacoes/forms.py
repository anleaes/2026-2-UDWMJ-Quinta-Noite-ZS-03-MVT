
from django import forms
from avaliacoes.models import EstacaoAtendimento


class EstacaoAtendimentoForm(forms.ModelForm):

    # Define os campos utilizados no formulário de cadastro e edição.
    class Meta:
        model = EstacaoAtendimento

        fields = [
            'identificacao',
            'numero_cadeira',
            'ambiente',
            'possui_lavatorio',
            'higienizada',
            'foto_espaco',
        ]

        # Personaliza os campos apresentados ao usuário.
        widgets = {
            'identificacao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Identificação da estação',
            }),
            'numero_cadeira': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
            }),
            'ambiente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Sala principal',
            }),
            'possui_lavatorio': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'higienizada': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'foto_espaco': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

        # Define os campos obrigatórios.
        labels = {
            'identificacao': 'Identificação',
            'numero_cadeira': 'Número da cadeira',
            'ambiente': 'Ambiente',
            'possui_lavatorio': 'Possui lavatório',
            'higienizada': 'Higienizada',
            'foto_espaco': 'Foto do espaço',
        }
