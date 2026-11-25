
from datetime import datetime, timedelta

from django.test import SimpleTestCase

from agendamentos.forms import AgendamentoForm


class AgendamentoFormTest(SimpleTestCase):

    # Prepara os dados diretamente para testar a validação de horários.
    def criar_formulario(self, inicio, fim):
        form = AgendamentoForm()

        form.cleaned_data = {
            'data_hora_inicio': inicio,
            'data_hora_fim': fim,
        }

        return form

    # Verifica se o formulário rejeita término anterior ao início.
    def test_horario_fim_anterior_ao_inicio(self):
        inicio = datetime(2026, 11, 25, 10, 0)
        fim = inicio - timedelta(minutes=30)

        form = self.criar_formulario(inicio, fim)
        form.clean()

        self.assertIn('data_hora_fim', form.errors)

    # Verifica se o formulário rejeita término igual ao início.
    def test_horario_fim_igual_ao_inicio(self):
        inicio = datetime(2026, 11, 25, 10, 0)

        form = self.criar_formulario(inicio, inicio)
        form.clean()

        self.assertIn('data_hora_fim', form.errors)

    # Verifica se o formulário aceita término posterior ao início.
    def test_horario_fim_posterior_ao_inicio(self):
        inicio = datetime(2026, 11, 25, 10, 0)
        fim = inicio + timedelta(hours=1)

        form = self.criar_formulario(inicio, fim)
        form.clean()

        self.assertNotIn('data_hora_fim', form.errors)
