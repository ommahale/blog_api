from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post
# Create your views here.

class PostList(generics.ListCreateAPIView):
    serializer_class=PostSerializer
    queryset=Post.postobjects.all()

class PostDetail(generics.RetrieveDestroyAPIView):
    serializer_class=PostSerializer
    queryset=Post.postobjects.all()
    
""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""