from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogPostList(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'core/blog_post_list.html'

    def get_queryset(self, *a, **kw):
        qs = super().get_queryset(*a, **kw)
        return qs.order_buy('created_at')


class BlogPostDetail(DetailView):
    context_object_name = 'post'
    model = BlogPost
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'core/blog_post_detail.html'
