from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def index(request):
    posts = (
        Post.objects
        .select_related('category', 'location', 'author')
        .filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        )
        .order_by('-pub_date')[:5]
    )

    return render(
        request,
        'blog/index.html',
        {
            'title': 'Главная страница',
            'posts': posts,
        }
    )


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        pk=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )

    return render(
        request,
        'blog/post_detail.html',
        {
            'title': post.title,
            'post': post,
        }
    )


def category_posts(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug,
        is_published=True
    )

    posts = (
        Post.objects
        .select_related('category', 'location', 'author')
        .filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now(),
        )
    )

    return render(
        request,
        'blog/category.html',
        {
            'title': f'Публикации в категории — {category.title}',
            'category': category,
            'posts': posts,
        }
    )
