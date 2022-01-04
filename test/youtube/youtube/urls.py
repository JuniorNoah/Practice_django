from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('testapp.urls')),
    path('sex/', include('select_sex.urls')),
    path('headtext/', include('headtext.urls')),
]