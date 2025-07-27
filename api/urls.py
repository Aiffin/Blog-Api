from django.urls import path
from .views import BlogApi,CommentApi

urlpatterns = [
    path('blog/',BlogApi.as_view()),
    path('comments/',CommentApi.as_view()),

]
