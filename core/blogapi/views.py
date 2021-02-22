from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.

class PostListView(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    

