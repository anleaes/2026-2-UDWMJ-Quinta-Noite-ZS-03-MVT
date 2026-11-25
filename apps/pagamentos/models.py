
from django.db import models


class PagamentoSalao(models.Model):

    # Cada pagamento pertence a um único agendamento.
    # O OneToOneField permite apenas um pagamento por agendamento.
    agendamento = models.OneToOneField(
        'agendamentos.Agendamento',
        on_delete=models.CASCADE,
        verbose_name='Agendamento'
    )

    # Valor total dos serviços realizados.
    valor_total_servicos = models.DecimalField(
        'Valor Total dos Serviços (R$)',
        max_digits=8,
        decimal_places=2
    )

    # Gorjeta destinada ao profissional.
    gorjeta_profissional = models.DecimalField(
        'Gorjeta do Profissional (R$)',
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # Formas de pagamento aceitas pelo salão.
    FORMA_PAGAMENTO_CHOICES = [
        ('DINHEIRO', 'Dinheiro'),
        ('PIX', 'PIX'),
        ('CREDITO', 'Cartão de Crédito'),
        ('DEBITO', 'Cartão de Débito'),
    ]

    forma_pagamento = models.CharField(
        'Forma de Pagamento',
        max_length=10,
        choices=FORMA_PAGAMENTO_CHOICES
    )

    # Informa se o pagamento foi realizado.
    pago = models.BooleanField(
        'Pago',
        default=False
    )

    # Data e hora do registro do pagamento.
    data_pagamento = models.DateTimeField(
        'Data do Pagamento',
        auto_now_add=True
    )

    # Comprovante de pagamento via PIX em PDF.
    comprovante_pix_pdf = models.FileField(
        'Comprovante PIX (PDF)',
        upload_to='pagamentos/comprovantes',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-data_pagamento']

    def __str__(self):
        return f"Pagamento {self.id} - R$ {self.valor_total_servicos}"
