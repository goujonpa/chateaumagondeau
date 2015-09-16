# Django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Import REST
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Import News
from news.models import New
from news.serializers import NewSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def news_list(request):
    """
    List all news, or create a new one.
    """
    if request.method == 'GET':
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def news_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        news = New.objects.get(pk=pk)
    except New.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewSerialiser(news)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NewSerialiser(news, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        news.delete()
        return HttpResponse(status=204)
