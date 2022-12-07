from django.db import models

# Create your models here.


class Pokemon(models.Model):

    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    ibge = models.CharField(max_length=20)
    gia = models.CharField(max_length=20)
    ddd = models.CharField(max_length=2)
    siafi = models.CharField(max_length=20)
