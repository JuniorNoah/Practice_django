from rest_framework.viewsets import ModelViewSet
from .models import CommunityModel
from .serializers import CommunitySerializer

class CommunityViewSet(ModelViewSet) :
    queryset = CommunityModel.objects.all()
    serializer_class = CommunitySerializer
    
community_list = CommunityViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

community_datail = CommunityViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})