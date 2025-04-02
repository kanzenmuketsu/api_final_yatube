# TODO:  Напишите свой вариант
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import exceptions

from posts.models import Group, Post
from .serializers import GroupSerializer, PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        author = self.get_object().author
        if author == self.request.user:
            serializer.save()
        else:
            raise exceptions.PermissionDenied()

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()
        else:
            raise exceptions.PermissionDenied()
