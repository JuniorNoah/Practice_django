from django.db import models
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import HeadModel, CommentModel, CommunityModel, PostModel
from block.serializers import BlockSerializer

class HeadSerializer(serializers.ModelSerializer) :
    class Meta :
        model = HeadModel
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = CommentModel
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer) :
    comment_post = CommentSerializer(many=True, read_only=True)
    
    class Meta :
        model = PostModel
        fields = '__all__'
                
class CommunitySerializer(serializers.ModelSerializer) :
    head_community = PrimaryKeyRelatedField(many=True, read_only=True)
    post_community = PrimaryKeyRelatedField(many=True, read_only=True)
    block = PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta :
        model = CommunityModel
        fields = '__all__'