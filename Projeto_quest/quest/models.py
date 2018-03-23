from django.db import models
from django.urls import reverse

class Questionario(models.Model):
    data_entrada = models.DateField(auto_now=True)
    data_final = models.DateField()
    titulo = models.CharField(max_length=50)


class Perguntas(models.Model):
    texto = models.CharField(max_length=150)

    class Meta:
        ordering = ["-texto"]

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('perguntas', kwargs={'pk': self.pk})


class Resposta(models.Model):
    valor = models.PositiveIntegerField()

class Visitante(models.Model):
    email = models.EmailField(max_length=254)