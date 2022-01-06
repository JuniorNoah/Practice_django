from django.urls import path
from .views import LoginListView

urlpatterns = [
    path('', LoginListView.as_view()),
]