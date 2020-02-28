from rest_framework import serializers
from .models import DefineModel


class DefineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefineModel
        fields = ('word',)
