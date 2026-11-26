from django.db import models
from categorias.models import Categoria


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=150)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Categoria',
    )
    marca = models.CharField('Marca', max_length=100, blank=True, null=True)
    descricao = models.TextField('Descrição', blank=True, null=True)
    preco = models.DecimalField('Preço (R$)', max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField('Estoque', default=0)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return self.nome