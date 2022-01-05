from rest_framework import serializers
from .models import UserModel
from select_sex.serializers import SelectSexSerializer

class UserSerializer(serializers.ModelSerializer) :
    # sex_selection = SelectSexSerializer(read_only=True)
    class Meta :
        model = UserModel
        fields = ('login_id', 'login_pw', 'email', 'name', 'nickname', 'sex_selection')