from django.urls import path
from .views import File, Comment, User


urlpatterns = [
    path('files/', File.as_view()),
    path('comments/', Comment.as_view()),
    path('users/', User.as_view())
]