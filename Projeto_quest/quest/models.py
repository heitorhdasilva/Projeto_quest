from django.db import models

class Questionario(models.Model):
    id_quest = models.AutoField(primary_key=True)
    data_entrada = models.DateField(auto_now=True)
    data_final = models.DateField()
    titulo = models.CharField(max_length=50)


class Perguntas(models.Model):
    id_pergunta = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=150)


class Resposta(models.Model):
    id_resposta = models.AutoField( primary_key=True)
    valor = models.PositiveIntegerField()

class Visitante(models.Model):
    id_resposta = models.AutoField( primary_key=True)
    email = models.EmailField(max_length=254)