from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogPostList(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'core/blog_post_list.html'


class BlogPostDetail(DetailView):
    context_object_name = 'post'
    model = BlogPost
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'core/blog_post_detail.html'
