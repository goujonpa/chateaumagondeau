from django.db import models


class News(models.Model):
    titre = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de parution')
    auteur = models.CharField(max_length=255)
    categorie = models.ForeignKey('Categorie')
    texte = models.TextField()

    def __unicode__(self):
        return self.titre


class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.titre
