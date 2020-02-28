from rest_framework import serializers
from .models import AudioModel


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioModel
        fields = ('word', 'language',)
