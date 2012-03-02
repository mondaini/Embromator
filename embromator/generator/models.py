from django.db import models

class Trecho(models.Model):
    text = models.CharField(max_length=50)
    coluna = models.IntegerField()

    class Meta:
        verbose_name = 'Trecho'
        verbose_name_plural = 'Trechos'