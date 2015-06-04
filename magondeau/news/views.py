from django.shortcuts import render
from news.models import News, Categorie


def home(request):
    news = News.objects.all()
    return render(request, 'news/home.html', {'news': news})
