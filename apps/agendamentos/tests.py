
from datetime import datetime, timedelta

from django.test import SimpleTestCase

from agendamentos.forms import AgendamentoForm


class AgendamentoFormTest(SimpleTestCase):

    # Verifica se o formulário rejeita término anterior ao início.
    def test_horario_fim_anterior_ao_inicio(self):
        inicio = datetime(2026, 11, 25, 10, 0)
        fim = inicio - timedelta(minutes=30)

        form = AgendamentoForm(data={
            'data_hora_inicio': inicio.strftime('%Y-%m-%dT%H:%M'),
            'data_hora_fim': fim.strftime('%Y-%m-%dT%H:%M'),
            'status_agendamento': 'AGENDADO',
            'confirmado_whatsapp': False,
            'observacoes_cliente': '',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('data_hora_fim', form.errors)

    # Verifica se o formulário aceita término posterior ao início.
    def test_horario_fim_posterior_ao_inicio(self):
        inicio = datetime(2026, 11, 25, 10, 0)
        fim = inicio + timedelta(hours=1)

        form = AgendamentoForm(data={
            'data_hora_inicio': inicio.strftime('%Y-%m-%dT%H:%M'),
            'data_hora_fim': fim.strftime('%Y-%m-%dT%H:%M'),
            'status_agendamento': 'AGENDADO',
            'confirmado_whatsapp': False,
            'observacoes_cliente': '',
        })

        self.assertNotIn('data_hora_fim', form.errors)
