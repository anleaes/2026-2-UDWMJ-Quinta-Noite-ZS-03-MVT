from django.db import models


class Categoria(models.Model):
    nome = models.CharField('Nome da Categoria', max_length=100, unique=True)
    descricao = models.TextField('Descrição', max_length=300)
    area_estetica = models.CharField('Área Estética', max_length=100, blank=True, default='')
    exige_biosseguranca = models.BooleanField('Exige Biossegurança / EPI', default=False)
    ativa = models.BooleanField('Ativa', default=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.nome