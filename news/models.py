from django.db import models


class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


class New(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    linked = models.CharField(max_length=30)
    categorie = models.ForeignKey(Categorie)
