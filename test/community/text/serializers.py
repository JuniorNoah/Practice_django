from django.db.models import fields
from rest_framework import serializers
from .models import TextModel

class TextSerializer(serializers.ModelSerializer) :
    class Meta :
        model = TextModel
        fields = '__all__'