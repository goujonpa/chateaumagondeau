from django.shortcuts import render
from news.models import News, Categorie


def home(request):
    news = News.objects.all().order_by('-date')[:5]
    return render(request, 'news/home.html', {'news': news})


def article(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news/article.html', {'article': news})
