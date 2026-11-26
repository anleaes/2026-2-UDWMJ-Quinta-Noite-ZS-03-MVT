from django.db import models
from pessoas.models import Pessoa

# Create your models here.
class Cliente(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='cliente',
        verbose_name='Pessoa',
    )
    data_cadastro = models.DateField('Data de Cadastro', auto_now_add=True)
    preferencias = models.TextField('Preferências / Observações', blank=True, null=True)
    pontos_fidelidade = models.PositiveIntegerField('Pontos de Fidelidade', default=0)
    ativo = models.BooleanField('Ativo', default=True)