import factory
from blog.models import Post
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', '123456')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f'Post Title {n}')
    # Remove the slug generation here if it's auto-generated
    # slug = factory.Faker('slug')  # This line can be removed if slug is auto-generated
    author = factory.SubFactory(UserFactory)
    status = 1
