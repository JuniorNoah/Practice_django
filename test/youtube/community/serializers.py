from rest_framework import serializers
from .models import CommunityModel

class CommunitySerializer(serializers.ModelSerializer) :
    class Meta :
        model = CommunityModel
        fields = '__all__'