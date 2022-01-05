from rest_framework import serializers
from .models import SelectSexModel

class SelectSexSerializer(serializers.ModelSerializer) :   
    class Meta :
        model = SelectSexModel
        exclude = ['id']
