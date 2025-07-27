from rest_framework import generics
from Blogs.models import Blog,Comment
from Blogs.serializers import BlogSerializer,CommentSerializer


class BlogApi(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
  

class CommentApi(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer


