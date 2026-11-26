
from django.db import models


class EstacaoAtendimento(models.Model):

    # Identificação da estação dentro do salão.
    identificacao = models.CharField(
        'Identificação',
        max_length=50
    )

    # Número da cadeira disponível na estação.
    numero_cadeira = models.IntegerField(
        'Número da Cadeira'
    )

    # Ambiente onde a estação está localizada.
    ambiente = models.CharField(
        'Ambiente',
        max_length=100
    )

    # Informa se a estação possui lavatório.
    possui_lavatorio = models.BooleanField(
        'Possui Lavatório'
    )

    # Informa se a estação está higienizada.
    higienizada = models.BooleanField(
        'Higienizada'
    )

    # Fotografia do espaço da estação.
    foto_espaco = models.ImageField(
        'Foto do Espaço',
        upload_to='estacoes/fotos',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Estação de Atendimento'
        verbose_name_plural = 'Estações de Atendimento'
        ordering = ['identificacao']

    def __str__(self):
        return self.identificacao
