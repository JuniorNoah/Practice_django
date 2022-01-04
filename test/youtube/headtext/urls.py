from django.urls import path
from .views import HeadDetailView, HeadListView

urlpatterns = [
    path('tools/', HeadListView.as_view()),
    path('tools/<int:head_id>/', HeadDetailView.as_view()),
]