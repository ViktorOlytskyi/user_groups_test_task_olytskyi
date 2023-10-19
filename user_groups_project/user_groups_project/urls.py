from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', include('groups.urls')),
    path('users/', include('users.urls')),
    path('', lambda request: redirect('user_list')),
]
