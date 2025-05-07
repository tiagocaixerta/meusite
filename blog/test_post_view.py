from django.test import TestCase
from blog.models import Post
from blog.factories import PostFactory

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = PostFactory()
        self.assertIsNotNone(post.id)
        self.assertGreater(len(post.title), 0)
