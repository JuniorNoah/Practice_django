from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import UserModel
from block.models import Blacklist
from .serializers import HeadSerializer, PostSerializer, CommentSerializer, CommunitySerializer
from .models import CommunityModel, PostModel, HeadModel, CommentModel

class HeadListView(APIView) :
    def get(self, request) :
        model = HeadModel.objects.all()
        serializer = HeadSerializer(model, many=True)
        return Response(serializer.data, status=201)

    def post(self, request) :
        user = UserModel.objects.filter(connection=True).first()
        community_id = request.data['head_community_id']
        
        admin = CommunityModel.objects.filter(id=community_id)
        if user.id == admin.filter(id=community_id).first().community_admin_id.id :
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
        user = UserModel.objects.filter(connection=True).first()
        head = HeadModel.objects.filter(id=head_id)
        admin = head.filter(id=head_id).first().head_community_id
        
        if user.id == admin.id :
            model = HeadModel.objects.filter(id=head_id).first()
            serializer = HeadSerializer(model, data=request.data, partial=True)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response('Not permission', status=401)
        
    def delete(self, request, head_id) :
        user = UserModel.objects.filter(connection=True).first()
        head = HeadModel.objects.filter(id=head_id)
        admin = head.filter(id=head_id).first().head_community_id
        
        if user.id ==  admin.id:
            model = HeadModel.objects.filter(id=head_id)
            model.delete()
            serializer = HeadSerializer(model, many=True)
            return Response(serializer.data, status=201)

class PostListView(APIView) :
    def get(self, request) :
        model = PostModel.objects.all()
        serializer = PostSerializer(model, many=True)
        return Response(serializer.data, status=201)

    def post(self, request) :
        user = UserModel.objects.filter(connection=True).first()
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid() :
            serializer.save()
            serializer.save(post_author_id=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostDetailView(APIView) :
    def get(self, request, post_id) :
        model = PostModel.objects.get(id=post_id)
        model.view_count += 1
        model.save()
        
        model = PostModel.objects.filter(id=post_id)
        serializer = PostSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, post_id) :
        user = UserModel.objects.filter(connection=True).first()
        post = PostModel.objects.filter(id=post_id)
        
        if user.id == post.filter(id=post_id).first().post_author_id.id :
            model = PostModel.objects.filter(id=user.id).first()
            serializer = PostSerializer(model, data=request.data, partial=True)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, post_id) :
        user = UserModel.objects.filter(connection=True).first()    
        post = PostModel.objects.filter(id=post_id)
        
        if user.id == post.filter(id=post_id).first().post_author_id.id :
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
        user = UserModel.objects.filter(connection=True).first()
        serializer = CommentSerializer(data=request.data, partial=True)
        
        if serializer.is_valid() :
            serializer.save()
            serializer.save(comment_author_id=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommentDetailView(APIView) :
    def get(self, request, comment_id) :
        model = CommentModel.objects.filter(id=comment_id)
        serializer = CommentSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, comment_id) :
        user = UserModel.objects.filter(connection=True).first()   
        comment = CommentModel.objects.filter(id=comment_id)
        
        if user.id == comment.filter(id=comment_id).first().comment_post_id.id :
            model = CommentModel.objects.filter(id=comment_id).first()
            serializer = CommentSerializer(model, data=request.data, partial=True)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, comment_id) :
        user = UserModel.objects.filter(connection=True).first()
        comment = CommentModel.objects.filter(id=comment_id)
        
        if user.id == comment.filter(id=comment_id).first().comment_author_id.id :
            model = CommentModel.objects.filter(id=comment_id)
            model.delete()
            serializer = CommentSerializer(model, many=True)
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
        serializer = CommunitySerializer(data=request.data, partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 

class CommunityDetailView(APIView) :
    def get(self, request, community_id) :
        user = UserModel.objects.filter(connection=True).first()
        black = Blacklist.objects.filter(blocked_id=user.id)
        
        if black.exists() :
            return Response('You are blocked this community', status=401)
        
        model = CommunityModel.objects.filter(id=community_id)
        serializer = CommunitySerializer(model, many=True)
        return Response(serializer.data)
        
    def delete(self, request, community_id) :
        user = UserModel.objects.filter(connection=True).first()
        model = CommunityModel.objects.filter(id=community_id)
        if user.id == model.filter(id=community_id).first().community_admin_id.id :
            model.delete()
            serializer = CommunitySerializer(model, many=True)
            return Response(serializer.data, status=201)
        return Response('Not permission', status=401)