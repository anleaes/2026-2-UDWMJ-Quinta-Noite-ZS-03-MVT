from decimal import Decimal

from django.test import SimpleTestCase

from atendimentos.forms import ItemAgendamentoForm


class ItemAgendamentoFormTest(SimpleTestCase):

    # Prepara os valores diretamente para testar a validação do desconto.
    def criar_formulario(self, valor, desconto):
        form = ItemAgendamentoForm()

        form.cleaned_data = {
            'valor_cobrado': Decimal(valor),
            'desconto_aplicado': Decimal(desconto),
        }

        return form

    # Verifica se o formulário rejeita desconto maior que o valor cobrado.
    def test_desconto_maior_que_valor(self):
        form = self.criar_formulario('100.00', '120.00')
        form.clean()

        self.assertIn('desconto_aplicado', form.errors)

    # Verifica se o formulário aceita desconto menor que o valor cobrado.
    def test_desconto_valido(self):
        form = self.criar_formulario('100.00', '20.00')
        form.clean()

        self.assertNotIn('desconto_aplicado', form.errors)

    # Verifica se o formulário aceita desconto igual ao valor cobrado.
    def test_desconto_igual_ao_valor(self):
        form = self.criar_formulario('100.00', '100.00')
        form.clean()

        self.assertNotIn('desconto_aplicado', form.errors)