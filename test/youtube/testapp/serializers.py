from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserModel
        fields = ('id', 'login_id', 'login_pw', 'email', 'name', 'nickname', 'sex_selection')