from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SelectSexSerializer
from .models import SelectSexModel

class SelectListView(APIView) :
    def get(self, request) :
        model = SelectSexModel.objects.all()
        serializer = SelectSexSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request) :
        serializer = SelectSexSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SelectDetailView(APIView) :
    def get(self, request, sex_id) :
        model = SelectSexModel.objects.filter(id=sex_id)
        serializer = SelectSexSerializer(SelectSexModel)
        return Response(serializer.data)
        
    def put(self, request, sex_id) :
        model = SelectSexModel.objects.filter(id=sex_id)
        serializer = SelectSexSerializer(model, data=request.data)
        if serializer.is_valid() :
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    def delete(self, sex_id) :
        model = SelectSexModel.objects.filter(id=sex_id)
        model.delete()
        serializer = SelectSexSerializer(model, many=True)
        return Response(serializer.data)