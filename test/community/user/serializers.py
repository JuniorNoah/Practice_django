from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer) :
    event = serializers.SerializerMethodField

    def get_event(self, instance) :
        return True if instance.age < 30 else False
    
    class Meta :
        model = UserModel
        fields = '__all__'