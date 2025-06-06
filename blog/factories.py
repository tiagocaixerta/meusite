import factory
from faker import Factory as FakerFactory
from django.utils.timezone import now
from blog.models import Post

faker = FakerFactory.create()

class PostFactory(factory.django.DjangoModelFactory):
    titulo = factory.LazyAttribute(lambda x: faker.sentence(nb_words=6))
    conteudo = factory.LazyAttribute(lambda x: faker.paragraph(nb_sentences=3))
    criado_em = factory.LazyFunction(now)  

    class Meta:
        model = Post
