from django.shortcuts import render


def news_tool(request):
    return render(request, 'news/news_tool.html', locals())
