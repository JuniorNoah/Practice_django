from django.urls import path
from .views import TextDetailView, TextListView

urlpatterns = [
    path('tools/', TextListView.as_view()),
    path('tools/<int:text_id>/', TextDetailView.as_view()),
]