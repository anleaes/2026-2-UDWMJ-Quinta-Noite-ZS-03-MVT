
from decimal import Decimal

from django.test import TestCase

from atendimentos.forms import ItemAgendamentoForm


class ItemAgendamentoFormTest(TestCase):

    # Verifica se o formulário rejeita desconto maior que o valor cobrado.
    def test_desconto_maior_que_valor(self):
        form = ItemAgendamentoForm(data={
            'valor_cobrado': Decimal('100.00'),
            'desconto_aplicado': Decimal('120.00'),
            'tempo_real_minutos': 60,
            'quimica_utilizada': '',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('desconto_aplicado', form.errors)

    # Verifica se o formulário aceita um desconto válido.
    def test_desconto_valido(self):
        form = ItemAgendamentoForm(data={
            'valor_cobrado': Decimal('100.00'),
            'desconto_aplicado': Decimal('20.00'),
            'tempo_real_minutos': 60,
            'quimica_utilizada': '',
        })

        self.assertNotIn('desconto_aplicado', form.errors)
