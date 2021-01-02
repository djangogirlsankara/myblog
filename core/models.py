from django.db import models


class BlogPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blog_posts')

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
