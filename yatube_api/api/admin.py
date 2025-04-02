from django.contrib import admin
from posts.models import Comment, Group, Follow, Post
# Register your models here.
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Group)
admin.site.register(Post)
