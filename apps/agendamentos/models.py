
from django.db import models


class Agendamento(models.Model):

    # Cliente responsável pelo agendamento.
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        verbose_name='Cliente'
    )

    # Profissional responsável pelo atendimento.
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        verbose_name='Profissional'
    )

    # Estação onde o atendimento será realizado.
    estacao = models.ForeignKey(
        'estacoes.EstacaoAtendimento',
        on_delete=models.CASCADE,
        verbose_name='Estação de Atendimento'
    )

    # Procedimentos associados ao agendamento.
    # A tabela intermediária ItemAgendamento guarda os detalhes de cada procedimento.
    servicos_agendados = models.ManyToManyField(
        'procedimentos.Procedimento',
        through='atendimentos.ItemAgendamento',
        verbose_name='Serviços Agendados'
    )

    # Data e horário de início e término.
    data_hora_inicio = models.DateTimeField('Data e Hora de Início')
    data_hora_fim = models.DateTimeField('Data e Hora de Término')

    # Situação atual do agendamento.
    STATUS_CHOICES = [
        ('AGENDADO', 'Agendado'),
        ('CONFIRMADO', 'Confirmado'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]

    status_agendamento = models.CharField(
        'Status do Agendamento',
        max_length=20,
        choices=STATUS_CHOICES,
        default='AGENDADO'
    )

    # Informa se o agendamento foi confirmado pelo WhatsApp.
    confirmado_whatsapp = models.BooleanField(
        'Confirmado pelo WhatsApp',
        default=False
    )

    # Observações informadas pelo cliente.
    observacoes_cliente = models.TextField(
        'Observações do Cliente',
        blank=True
    )

    # Data e hora em que o registro foi criado.
    criado_em = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['data_hora_inicio']

    def __str__(self):
        return f"Agendamento {self.id} - {self.data_hora_inicio}"
