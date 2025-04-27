from blog.models import Post
from django.contrib.auth.models import User
from django.utils.text import slugify  # Importar slugify para gerar o slug

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Corrigi 'title' para ser mais padronizado
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Corrigi 'slug' para permitir vazio inicialmente
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # Alterei o related_name para 'blog_posts'
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']  # Ordenação por data de criação (descendente)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Só gera o slug se ele ainda não existir
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)  # Chama o save original para salvar o objeto
