from django.urls import path
from .views import CommentListView,  CommentDetailView
urlpatterns = [
    path('tools/', CommentListView.as_view()),
    path('tools/<int:comment_id>', CommentDetailView.as_view()),
]
