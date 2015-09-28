# Django imports
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

# Import REST
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Import News
from news.models import New
from news.serializers import NewSerializer


class NewsList(APIView):
    """
    Provides a list the news
    """

    def get(self, request, format=None):
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetail(APIView):
    """
    Retrieve, update or delete a news.
    """

    def get_object(self, pk):
        try:
            return New.objects.get(pk=pk)
        except New.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        New = get_object(pk)
        serializer = NewSerializer(new)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        New = get_object(pk)
        serializer = NewSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        New = get_object(pk)
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
