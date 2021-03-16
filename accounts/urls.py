from django.urls import path, include
from .views import LoginAPI

urlpatterns = [
    path('api/auth/login', LoginAPI.as_view()),
]