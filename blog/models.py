from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Permitir slug vazio para gerar automaticamente
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)  # 1 = publicado, 0 = rascunho

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # Gera o slug automaticamente baseado no título
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
