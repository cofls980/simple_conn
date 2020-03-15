from .models import Text, Color
from rest_framework import serializers


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
