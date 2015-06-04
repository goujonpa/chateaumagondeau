from django.db import models


class News(models.Model):
    titre = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de parution')
    auteur = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)
    texte = models.TextField()

    def __str__(self):
        return self.titre
