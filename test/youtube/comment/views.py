from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommentSerializer
from .models import CommentModel

class CommentListView(APIView) :
    def get(self, request) :
        model = CommentModel.objects.all()
        serializer = CommentSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommentDetailView(APIView) :
    def get(self, request, comment_id) :
        model = CommentModel.objects.filter(id=comment_id)
        serializer = CommentSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, comment_id) :
        model = CommentModel.objects.filter(id=comment_id).first()
        serializer = CommentSerializer(model, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, comment_id) :
        model = CommentModel.objects.filter(id=comment_id)
        model.delete()
        serializer = CommentSerializer(model, many=True)
        return Response(serializer.data)
