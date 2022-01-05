from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path('tools/', UserListView.as_view()),
    path('tools/<int:user_id>/', UserDetailView.as_view()),
]