from django.urls import path
from .views import HeadListView, HeadDetailView
from .views import PostListView, PostDetailView
from .views import CommentListView, CommentDetailView
from .views import CommunityListView, CommunityDetailView

urlpatterns = [
    path('home/', CommunityListView.as_view()),
    path('home/<int:community_id>/', CommunityDetailView.as_view()),
    
    path('head/', HeadListView.as_view()),
    path('head/<int:head_id>', HeadDetailView.as_view()),
    
    path('post/', PostListView.as_view()),
    path('post/<int:post_id>', PostDetailView.as_view()),
    
    path('comment/', CommentListView.as_view()),
    path('comment/<int:comment_id>', CommentDetailView.as_view()),
]