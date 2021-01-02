from django.views.generic import ListView

from .models import BlogPost


class BlogPostList(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'core/blog_post_list.html'
