from rest_framework import serializers
from .models import MainPage

class MainSerializer(serializers.ModelSerializer) :
    event = serializers.SerializerMethodField
    
    class Meta :
        model = MainPage
        fields = '__all__'