
from django.test import SimpleTestCase

from pagamentos.forms import PagamentoSalaoForm


class PagamentoSalaoFormTest(SimpleTestCase):

    # Verifica se os campos de valores aceitam apenas valores não negativos na interface.
    def test_campos_valores_configurados_com_minimo_zero(self):
        form = PagamentoSalaoForm()

        self.assertEqual(
            form.fields['valor_total_servicos'].widget.attrs['min'],
            '0'
        )
        self.assertEqual(
            form.fields['gorjeta_profissional'].widget.attrs['min'],
            '0'
        )

    # Verifica se os campos monetários utilizam precisão de duas casas decimais.
    def test_campos_valores_configurados_com_duas_casas_decimais(self):
        form = PagamentoSalaoForm()

        self.assertEqual(
            form.fields['valor_total_servicos'].widget.attrs['step'],
            '0.01'
        )
        self.assertEqual(
            form.fields['gorjeta_profissional'].widget.attrs['step'],
            '0.01'
        )

    # Verifica se as formas de pagamento previstas estão disponíveis.
    def test_formas_de_pagamento_disponiveis(self):
        form = PagamentoSalaoForm()

        valores = [
            valor for valor, descricao
            in form.fields['forma_pagamento'].choices
            if valor
        ]

        self.assertEqual(
            valores,
            ['DINHEIRO', 'PIX', 'CREDITO', 'DEBITO']
        )

    # Verifica se o comprovante utiliza um campo de envio de arquivos.
    def test_comprovante_pix_permite_upload(self):
        form = PagamentoSalaoForm()

        self.assertEqual(
            form.fields['comprovante_pix_pdf'].widget.input_type,
            'file'
        )
