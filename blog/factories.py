import factory
from faker import Factory as FakerFactory

from django.utils.timezone import now
from blog.models import Post

faker = FakerFactory.create()

class PostFactory(factory.django.DjangoModelFactory):
    titulo = factory.LazyAttribute(lambda x: faker.sentence())
    conteudo = factory.Faker("text")
    criado_em = factory.LazyFunction(now)  # pode ser omitido, já que o modelo tem auto_now_add

    class Meta:
        model = Post
