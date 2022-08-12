from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register('groups', GroupViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
