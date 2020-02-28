from rest_framework import serializers
from .models import TranslateModel


class TranslateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslateModel
        fields = ('text', 'src', 'dest')
