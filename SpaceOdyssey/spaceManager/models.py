# https://docs.djangoproject.com/en/3.2/topics/db/models/

from django.db import models
from django.utils import timezone


class Pais(models.Model):
    nom = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.nom


class Agencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Missio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    descripcio = models.CharField(max_length=200)
    data_finalitzacio = models.DateTimeField(default=timezone.now)
    agencia = models.ForeignKey(Agencia, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom


class Nau(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    capacitat = models.IntegerField()
    agencia = models.ForeignKey(Agencia, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom


class Plataforma(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    pais = models.ForeignKey(Pais, on_delete=models.RESTRICT)
    agencia = models.ForeignKey(Agencia, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom


GENDER_CHOICES = [
    ('H', 'Home'),
    ('D', 'Dona'),
    ('?', 'Altre'),
]

BLOOD_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

class Astronauta(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    cognom = models.CharField(max_length=50)
    naixement = models.DateField(default=timezone.now)
    genere = models.CharField(max_length=1, choices=GENDER_CHOICES)
    altura = models.IntegerField()
    grup_sanguini = models.CharField(max_length=3, choices=BLOOD_CHOICES)
    pais = models.ForeignKey(Pais, on_delete=models.RESTRICT)
    agencia = models.ForeignKey(Agencia, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.nom) + ' ' + str(self.cognom)
