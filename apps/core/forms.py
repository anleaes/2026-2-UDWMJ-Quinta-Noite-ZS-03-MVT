
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CadastroUsuarioForm(UserCreationForm):
    # Campo para receber o nome completo do novo usuário.
    nome_completo = forms.CharField(
        label='Nome completo',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome completo',
        })
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail',
        })
    )

    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escolha um nome de usuário',
        })
    )

    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        })
    )

    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite novamente sua senha',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)

        # Separa o nome completo nos campos do usuário Django.
        partes_nome = self.cleaned_data['nome_completo'].strip().split()
        usuario.first_name = partes_nome[0]
        usuario.last_name = ' '.join(partes_nome[1:])
        usuario.email = self.cleaned_data['email']

        if commit:
            usuario.save()

        return usuario
