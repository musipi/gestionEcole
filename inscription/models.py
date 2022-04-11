import datetime

from django.db import models


# Create your models here.

class Etudiant(models.Model):
    nomEtudiant = models.CharField(max_length=50)
    postnomEtu = models.CharField(max_length=50)
    prenomEtud = models.CharField(max_length=50)
    telephone = models.IntegerField()
    genre = models.CharField(max_length=50)
    lieuNaissaince = models.CharField(max_length=50)
    dateNaissance = models.DateTimeField(datetime.datetime.now())
    adresseDomicile = models.TextField()
    nomTuteur = models.CharField(max_length=50)

class Promotion(models.Model):
    nomPromotion = models.CharField(max_length=50)
    filiere = models.CharField(max_length=50)
    createdAt = models.DateTimeField(datetime.datetime.now())

class Inscription(models.Model):
    nomEtudiant = models.ForeignKey(Etudiant, on_delete= models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    montantPayer = models.IntegerField()
    designation = models.TextField()
    createdAt = models.DateTimeField(datetime.datetime.now())

