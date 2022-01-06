from django.db import models
from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserModel
        fields = '__all__'
        
class LoginSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserModel
        fields = ('login_id', 'login_pw')