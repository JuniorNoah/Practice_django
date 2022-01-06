from rest_framework import serializers
from .models import HeadTextModel

class HeadtextSerializer(serializers.ModelSerializer) :
    class Meta :
        model = HeadTextModel
        fields = '__all__'