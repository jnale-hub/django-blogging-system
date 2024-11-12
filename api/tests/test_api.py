import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from blog.models import Author, Post, Comment

@pytest.fixture
def api_client():
    """Fixture to create an API client for testing."""
    return APIClient()

@pytest.fixture
def author():
    """Fixture to create a test author."""
    return Author.objects.create(name='Test Author', email='author@example.com')

@pytest.fixture
def post(author):
    """Fixture to create a test post."""
    return Post.objects.create(
        title='Test Post',
        content='This is a test post.',
        author=author,
        status=Post.PUBLISHED
    )

@pytest.mark.django_db
def test_list_posts(api_client, post):
    """Test that posts are listed using the API."""
    url = reverse('api_post_list')
    response = api_client.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert len(response.data) > 0, "Expected at least one post in the response"

@pytest.mark.django_db
def test_filter_posts_by_title(api_client, post):
    """Test that posts can be filtered by title."""
    url = reverse('api_post_list')
    response = api_client.get(url, {'search': 'Test Post'})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert len(response.data) == 1, "Expected one post with title 'Test Post'"

@pytest.mark.django_db
def test_filter_posts_by_author_name(api_client, post):
    """Test that posts can be filtered by author name."""
    url = reverse('api_post_list')
    response = api_client.get(url, {'search': 'Test Author'})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert len(response.data) == 1, "Expected one post by author 'Test Author'"

@pytest.mark.django_db
def test_create_post(api_client, author):
    """Test that a post can be created using the API."""
    url = reverse('api_post_list')
    data = {
        'title': 'New Post',
        'content': 'This is a new post.',
        'author': author.id,
        'status': Post.PUBLISHED
    }
    response = api_client.post(url, data)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    assert Post.objects.filter(title='New Post').exists(), "Expected the new post to be created"

@pytest.mark.django_db
def test_create_comment(api_client, post):
    """Test that a comment can be created on a post using the API."""
    url = reverse('api_comment_create')
    data = {
        'post': post.id,
        'content': 'This is a test comment.'
    }
    response = api_client.post(url, data)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    assert Comment.objects.filter(content='This is a test comment.').exists(), "Expected the new comment to be created"
