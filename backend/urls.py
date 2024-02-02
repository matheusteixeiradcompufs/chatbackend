from django.contrib import admin
from django.urls import path

from accounts.views import register_user, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user, name='register'),
    path('login/', login, name='login'),
]
