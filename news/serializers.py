from rest_framework import serializers
from news.models import New


class NewSerializer(serializers.ModelSerializer):
    """News Serializer
    Serializer for the New model in our REST API
    """

    class Meta:
        model = New
        fields = ('title', 'text', 'linked', 'categorie')
