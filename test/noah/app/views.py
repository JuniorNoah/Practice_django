from django.core.exceptions import *
from rest_framework import status, viewsets
from rest_framework.response import Response
from app.models import UserModel
from app.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet) :
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self) :
        return UserModel.objects.all()

    # it's related to 'POST' / write row from DB table
    def create(self, request, *args, **kwargs) :
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False) :
            serializer.save()
            return Response({"message": "Operate succesfully"}, status=status.HTTP_201_CREATED)
        else :
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    # it's related to 'GET' / read row from DB table
    def list(self, request) :
        # queryset = UserModel.objects.all()
        # serializer = UserSerial(queryset, many=True)
        # 이 주석으로도 데이터베이스의 테이블에서 값을 읽을 수도 있음.
        serializer = UserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # it's related to 'GET' / read(search) row from DB table
    def retrieve(self, request, uuid=None) :
        try :
            objects = UserModel.objects.get(id=uuid)
            serializer = UserSerializer(objects)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist :
            return Response({"message": "존재하지 않는 UUID({})".format(uuid)}, status=status.HTTP_404_NOT_FOUND)
    
    # it's related to 'PUT' / modify(insert) row from DB table    
    def update(self, request, uuid=None) :
        objects = UserModel.objects.get(id=uuid)
        serializer = UserSerializer(objects, data=request.data)
        if serializer.is_valid(raise_exception=False) :
            serializer.save()
            return Response({"message": "Operate successfully"}, status=status.HTTP_200_OK)
        else :
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # it's related to 'DELETE' / delete row from the DB table    
    def destroy(self, request, uuid=None) :
        objects = UserModel.objects.get(id=uuid)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
