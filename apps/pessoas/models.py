from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('Nome Completo', max_length=150)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True, help_text='Formato: DD/MM/AAAA')
    endereco = models.CharField('Endereço', max_length=250, blank=True, null=True)
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return f'{self.nome} ({self.cpf})'