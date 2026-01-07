import pytest
from django.urls import reverse
from blog.models import Category, Post
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


@pytest.mark.django_db
def test_index_url(client):
    response = client.get(reverse('blog:index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_url(client):
    user = User.objects.create(username='testuser')
    category = Category.objects.create(
        title='Test',
        description='Test',
        slug='test',
        is_published=True
    )
    post = Post.objects.create(
        title='Post',
        text='Text',
        pub_date=timezone.now(),
        author=user,
        category=category,
        is_published=True
    )

    response = client.get(reverse('blog:post_detail', args=[post.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_url(client):
    category = Category.objects.create(
        title='Personal',
        description='Personal',
        slug='personal',
        is_published=True
    )

    response = client.get(
        reverse('blog:category_posts', args=[category.slug])
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_about_page(client):
    response = client.get(reverse('pages:about'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_rules_page(client):
    response = client.get(reverse('pages:rules'))
    assert response.status_code == 200
