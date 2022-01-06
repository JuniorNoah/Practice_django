from django.db import models
from rest_framework import serializers
from .models import BlackList

class BlackSerializer(serializers.ModelSerializer) :
    class Meta :
        model = BlackList
        fields = '__all__'