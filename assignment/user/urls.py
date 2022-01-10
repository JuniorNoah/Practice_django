from django.urls import path
from .views import UserListView, UserDetailView, Loginview

urlpatterns = [
    path('crud/', UserListView.as_view()),
    path('crud/<int:user_id>/', UserDetailView.as_view()),
    path('login/', Loginview.as_view(), name='login'),
]