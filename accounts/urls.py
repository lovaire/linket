# accounts/urls.py
from django.urls import path
from .views import RegisterView

urlpatterns = [
    # Ini membuat URL: /accounts/register/
    path('register/', RegisterView.as_view(), name='register'),
]