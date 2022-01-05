from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('sex/', include('select_sex.urls')),
    path('headtext/', include('headtext.urls')),
    path('text/', include('text.urls')),
    path('blacklist/', include('black.urls')),
    path('comment/', include('comment.urls')),
    path('community/', include('community.urls')),
    path('login/', include('login.urls')),
]