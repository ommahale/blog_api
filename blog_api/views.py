from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions,BasePermission,SAFE_METHODS
# Create your views here.
class PostUserWritePermission(BasePermission):
    message='Editing post is restricted to author only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author==request.user

class PostList(generics.ListCreateAPIView):
    permission_classes=[DjangoModelPermissions]
    serializer_class=PostSerializer
    queryset=Post.postobjects.all()

class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
    permission_classes=[PostUserWritePermission]
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