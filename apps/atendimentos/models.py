
from django.db import models


class ItemAgendamento(models.Model):

    # Agendamento ao qual este item pertence.
    agendamento = models.ForeignKey(
        'agendamentos.Agendamento',
        on_delete=models.CASCADE,
        verbose_name='Agendamento'
    )

    # Procedimento associado ao agendamento.
    procedimento = models.ForeignKey(
        'procedimentos.Procedimento',
        on_delete=models.CASCADE,
        verbose_name='Procedimento'
    )

    # Valor cobrado pelo procedimento.
    valor_cobrado = models.DecimalField(
        'Valor Cobrado (R$)',
        max_digits=8,
        decimal_places=2
    )

    # Desconto aplicado ao procedimento.
    desconto_aplicado = models.DecimalField(
        'Desconto Aplicado (R$)',
        max_digits=8,
        decimal_places=2,
        default=0
    )

    # Tempo real utilizado na execução do procedimento.
    tempo_real_minutos = models.PositiveIntegerField(
        'Tempo Real (Minutos)',
        default=0
    )

    # Produtos químicos utilizados durante o procedimento.
    quimica_utilizada = models.TextField(
        'Química Utilizada',
        blank=True
    )

    # Fotos do procedimento antes e depois.
    foto_antes_depois = models.ImageField(
        'Foto Antes e Depois',
        upload_to='atendimentos/fotos',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Item de Agendamento'
        verbose_name_plural = 'Itens de Agendamento'
        ordering = ['id']

    def __str__(self):
        return f"{self.procedimento} - Agendamento {self.agendamento.id}"
