from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status')  # Adicione status se quiser ver na lista
    prepopulated_fields = {'slug': ('titulo',)}  # preenche slug automaticamente
    list_filter = ('status',)  # Filtro por status
    search_fields = ('titulo', 'conteudo')  # Habilita busca
    ordering = ('-id',)  # Ordenação
