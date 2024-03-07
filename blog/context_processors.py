from .models import Post


def recent_posts(request):
    recent_posts_sidebar = Post.objects.order_by('-date')[:5]
    return {'recent_posts': recent_posts_sidebar}
