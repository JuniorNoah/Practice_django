from rest_framework import serializers
from .models import HeadModel, CommentModel, CommunityModel, PostModel

class HeadSerializer(serializers.ModelSerializer) :
    class Meta :
        model = HeadModel
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PostModel
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = CommentModel
        fields = '__all__'
        
class CommunitySerializer(serializers.ModelSerializer) :
    class Meta :
        model = CommunityModel
        fields = ('id')