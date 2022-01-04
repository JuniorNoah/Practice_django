from django.urls import path
from .views import SelectListView, SelectDetailView

urlpatterns = [
    path('tools/', SelectListView.as_view()),
    path('tools/<int:sex_id>/', SelectDetailView.as_view())
]