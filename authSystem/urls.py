from django.urls import path
from .api import RegisterAPI, LoginAPI, CurrentUserAPI
urlpatterns = [
    path('api/users/register', RegisterAPI.as_view(), name='user-register'),
    path('api/current-user', CurrentUserAPI.as_view(), name='current-user'),
    path('api/users/login', LoginAPI.as_view(), name='user-login')
]
