from django.views import generic
from .models import Post

class PostView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1).order_by('-criado_em')  # Certifique-se que o campo 'criado_em' está correto no model

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
