from django.urls import path
from .views import PostListView, PostDetailView, CommentCreateView, PostUpdateView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='api_post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='api_post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='api_post_update'),
    path('comments/', CommentCreateView.as_view(), name='api_comment_create'),
]
