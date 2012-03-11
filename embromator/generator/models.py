from django.db import models

class Fragment(models.Model):
    text = models.CharField(max_length=50)
    column = models.IntegerField()

    class Meta:
        verbose_name = 'Fragment'
        verbose_name_plural = 'Fragments'