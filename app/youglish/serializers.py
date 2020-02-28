from rest_framework import serializers
from .models import YouglishModel


class YouglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouglishModel
        fields = ('text', 'language')
