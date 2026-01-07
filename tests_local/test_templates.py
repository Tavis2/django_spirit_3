import pytest
from django.urls import reverse
from blog.models import Category, Post
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


@pytest.mark.django_db
def test_index_template(client):
    response = client.get(reverse('blog:index'))
    assert 'blog/index.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_post_detail_template(client):
    user = User.objects.create(username='testuser')
    category = Category.objects.create(
        title='Test',
        description='Test',
        slug='test',
        is_published=True
    )
    post = Post.objects.create(
        title='Test post',
        text='Text',
        pub_date=timezone.now(),
        author=user,
        category=category,
        is_published=True
    )

    response = client.get(reverse('blog:post_detail', args=[post.id]))
    assert 'blog/post_detail.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_category_template(client):
    category = Category.objects.create(
        title='Travel',
        description='Travel',
        slug='travel',
        is_published=True
    )

    response = client.get(
        reverse('blog:category_posts', args=[category.slug])
    )
    assert 'blog/category.html' in [t.name for t in response.templates]
