from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]
