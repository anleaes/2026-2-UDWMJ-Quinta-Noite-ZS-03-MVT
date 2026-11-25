from django.db import models
from categorias.models import Categoria

class Procedimento(models.Model):
    nome = models.CharField('Nome do Procedimento', max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name='Categoria Técnica'
    )
    descricao = models.TextField('Descrição e Etapas', max_length=300)
    preco = models.DecimalField('Preço (R$)', max_digits=8, decimal_places=2)
    duracao_minutos = models.PositiveIntegerField('Duração Estimada (minutos)', default=60)
    exige_teste_mecha = models.BooleanField('Exige Teste de Mecha / Alergia', default=False)
    foto_inspiracao = models.ImageField(
        'Foto de Referência',
        upload_to='procedimentos/fotos',
        blank=True,
        null=True
    )
    protocolo_pop = models.FileField(
        'Protocolo Técnico (PDF)',
        upload_to='procedimentos/pop',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"