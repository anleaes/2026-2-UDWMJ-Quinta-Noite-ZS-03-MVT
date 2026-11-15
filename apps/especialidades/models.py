from django.db import models

class Especialidade(models.Model):
    nome = models.CharField('Nome da Especialidade', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)
    area_estetica = models.CharField('Área Estética (Cabelo, Unhas, Facial)', max_length=50)
    exige_biosseguranca = models.BooleanField('Exige Protocolo de Biossegurança', default=True)
    ativa = models.BooleanField('Ativa', default=True)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
        ordering = ['id']

    def __str__(self):
        return self.nome