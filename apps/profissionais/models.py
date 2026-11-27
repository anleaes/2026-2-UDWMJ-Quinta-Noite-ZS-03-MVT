from django.db import models
from pessoas.models import Pessoa


class Profissional(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='profissional',
        verbose_name='Pessoa',
    )
    especialidade = models.CharField('Especialidade', max_length=100, blank=True, null=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering = ['pessoa__nome']

    def __str__(self):
        return str(self.pessoa)