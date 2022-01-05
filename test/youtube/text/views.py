from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TextSerializer
from .models import TextModel

class TextListView(APIView) :
    def get(self, request) :
        model = TextModel.objects.all()
        serializer = TextSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TextDetailView(APIView) :
    def get(self, request, text_id) :
        model = TextModel.objects.filter(id=text_id)
        serializer = TextSerializer(model, many=True)
        return Response(serializer.data)
        
    def put(self, request, text_id) :
        model = TextModel.objects.filter(id=text_id).first()
        serializer = TextSerializer(model, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, text_id) :
        model = TextModel.objects.filter(id=text_id)
        model.delete()
        serializer = TextSerializer(model, many=True)
        return Response(serializer.data)
