HEAD
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# blog/models.py

class Post:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def __str__(self):
        return f"Post: {self.titulo}"
c36e5b6 (Implementa estrutura base do blog e configura a branch post-model)
