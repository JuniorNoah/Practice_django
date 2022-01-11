from rest_framework import serializers
from .models import Blacklist

class BlockSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Blacklist
        fields =  '__all__'
