from django.urls import path

from .views import BlogPostList

urlpatterns = [
    path('', BlogPostList.as_view(), name='blog-post-list')
]
