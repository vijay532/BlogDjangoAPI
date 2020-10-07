# The final step is to create our views. Django REST Framework has several generic
# views that are helpful.

from django.shortcuts import render

# Create your views here.


from rest_framework import generics,permissions

from .models import Post
from .serializers import PostSerializer

from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer