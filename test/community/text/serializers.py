from django.db.models import fields
from rest_framework import serializers
from user.serializers import UserSerializer
from .models import TextModel

class TextSerializer(serializers.ModelSerializer) :
    user = UserSerializer(many=True, read_only=True)
    
    class Meta :
        model = TextModel
        fields = '__all__'