from rest_framework.viewsets import ModelViewSet
from .models import UserModel
from .serializers import UserSerializer

class UserViewSet(ModelViewSet) :
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_datail = UserViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})