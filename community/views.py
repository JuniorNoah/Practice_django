from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.urls import reverse
from user.models import UserModel
from block.models import Blacklist
from .serializers import HeadSerializer, PostSerializer, CommentSerializer, CommunitySerializer
from .models import CommunityModel, PostModel, HeadModel, CommentModel

class HeadListView(APIView) :
    def get(self, request) :
        model = HeadModel.objects.all()
        serializer = HeadSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        user_id = UserModel.objects.filter(connection=True)['id']
        community_id = request.data['head_community_id']
        
        admin_id = CommunityModel.objects.filter(id=community_id)['community_admin_id']
        if user_id == admin_id :
            serializer = HeadSerializer(data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response(401)

class HeadDetailView(APIView) :
    def get(self, request, head_id) :
        model = HeadModel.objects.filter(id=head_id)
        serializer = HeadSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, head_id) :
        user_id = UserModel.objects.filter(connection=True)['id']
        community_id = request.data['head_community_id']
        
        admin_id = CommunityModel.objects.filter(id=community_id)['community_admin_id']
        if user_id == admin_id :
            model = HeadModel.objects.filter(id=head_id).first()
            serializer = HeadSerializer(model, data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
    def delete(self, request, head_id) :
        user_id = UserModel.objects.filter(connection=True)['id']
        community_id = request.data['head_community_id']
        
        admin_id = CommunityModel.objects.filter(id=community_id)['community_admin_id']
        if user_id == admin_id :
            model = HeadModel.objects.filter(id=head_id)
            model.delete()
            serializer = HeadSerializer(model, many=True)
            return Response(serializer.data)

class PostListView(APIView) :
    def get(self, request) :
        model = PostModel.objects.all()
        serializer = PostSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        user_id = UserModel.objects.filter(connection=True)['id']
        serializer = PostSerializer(data=request.data, partial=True, post_author_id=user_id)
        
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostDetailView(APIView) :
    def get(self, request, post_id) :
        model = PostModel.objects.filter(id=post_id)
        serializer = PostSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, post_id) :
        user_id = UserModel.objects.filter(connection=True)['id']       
        author_id = PostModel.objects.filter(id=post_id)['post_author_id'].first()
        
        if user_id == author_id :
            model = PostModel.objects.filter(id=user_id).first()
            serializer = PostSerializer(model, data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
    def delete(self, request, post_id) :
        user_id = UserModel.objects.filter(connection=True)['id']       
        author_id = PostModel.objects.filter(id=post_id)['post_author_id'].first()
        
        if user_id == author_id :
            model = PostModel.objects.filter(id=post_id)
            model.delete()
            serializer = PostSerializer(model, many=True)
            return Response(serializer.data)

class CommentListView(APIView) :
    def get(self, request) :
        model = CommentModel.objects.all()
        serializer = CommentSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        user_id = UserModel.objects.filter(connection=True)['id']
        serializer = CommentSerializer(data=request.data, partial=True, comment_author_id=user_id)
        
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommentDetailView(APIView) :
    def get(self, request, comment_id) :
        model = CommentModel.objects.filter(id=comment_id)
        serializer = HeadSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, comment_id) :
        user_id = UserModel.objects.filter(connection=True)['id']       
        author_id = PostModel.objects.filter(id=comment_id)['post_author_id'].first()
        
        if user_id == author_id :
            model = CommentModel.objects.filter(id=comment_id).first()
            serializer = HeadSerializer(model, data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
    def delete(self, request, comment_id) :
        user_id = UserModel.objects.filter(connection=True)['id']       
        author_id = PostModel.objects.filter(id=comment_id)['post_author_id'].first()
        
        if user_id == author_id :
            model = CommentModel.objects.filter(id=comment_id)
            model.delete()
            serializer = HeadSerializer(model, many=True)
            return Response(serializer.data)

class CommunityListView(APIView) :
    def get(self, request) :
        model = CommunityModel.objects.all()
        if model.exists() :
            serializer = CommunitySerializer(model, many=True)
            return Response(serializer.data, status=201)
        return Response('Type new community informations', status=400)               

    def post(self, request) :    
        admin = request.data['admin_name']
        
        serializer = CommunitySerializer(data=request.data)
        user = UserModel.objects.get(name=admin)

        if serializer.is_valid() and admin == user :
            serializer.save()
            serializer.save(community_admin_id=user['id'])
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommunityDetailView(APIView) :
    def get(self, request, community_id) :
        user_id = UserModel.objects.filter(connection=True)['id']
        black = Blacklist.objects.filter(blacked_id=user_id, comm_id=community_id)
        
        if black.exists() :
            return Response(400)
        
        model = CommunityModel.objects.filter(id=community_id)
        serializer = CommunitySerializer(model, many=True)
        return Response(serializer.data)
        
    def delete(self, request, community_id) :
        user = UserModel.objects.filter(connection=True).first()
        model = CommunityModel.objects.filter(id=community_id)
        if user == model['community_admin_id'] :
            model.delete()
            serializer = CommunitySerializer(model, many=True)
            return Response(serializer.data)
        return Response(status=401)