from rest_framework.viewsets import ModelViewSet
from .models import BlackList
from .serializers import BlackSerializer

class BlackViewSet(ModelViewSet) :
    queryset = BlackList.objects.all()
    serializer_class = BlackSerializer
    
black_list = BlackViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

black_datail = BlackViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})