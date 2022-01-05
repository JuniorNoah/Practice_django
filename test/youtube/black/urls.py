from django.urls import path
from .views import BlackListView, BlackDetailView

urlpatterns = [
    path('lists/', BlackListView.as_view()),
    path('lists/<int:user_id>/', BlackDetailView.as_view()),
]