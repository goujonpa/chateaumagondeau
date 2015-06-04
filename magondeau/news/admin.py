from django.contrib import admin
from news.models import News, Categorie


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass
