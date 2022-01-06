from rest_framework.viewsets import ModelViewSet
from .models import CommentModel
from .serializers import CommentSerializer

class CommentViewSet(ModelViewSet) :
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    
comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

comment_datail = CommentViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})