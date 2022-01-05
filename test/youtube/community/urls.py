from django.urls import path
from .views import CommListView, CommDetailView

urlpatterns = [
    path('tools/', CommListView.as_view()),
    path('tools/<int:comm_id>/', CommDetailView.as_view()),
]