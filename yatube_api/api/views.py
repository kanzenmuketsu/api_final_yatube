# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from posts.models import Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from .permissions import AuthorOrReadOnly


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        return self.get_post().comments.all()

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), author=self.request.user)
