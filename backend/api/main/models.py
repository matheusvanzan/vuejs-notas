from django.db import models

# Create your models here.
class Nota(models.Model):

    titulo = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=2000)
    ativa = models.BooleanField(default=True)