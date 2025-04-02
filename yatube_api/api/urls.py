from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet, basename='Group')
router.register('posts', PostViewSet, basename='Post')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]
