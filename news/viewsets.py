from rest_framework import viewsets
from news.serializers import NewSerializer
from news.models import New


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
