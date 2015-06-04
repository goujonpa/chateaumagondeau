from django.shortcuts import render
from news.models import News, Categorie


def home(request):
    news = News.objects.all().order_by('date').reverse()[:5]
    return render(request, 'news/home.html', {'news': news})
