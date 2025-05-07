from blog.models import Post

posts = Post.objects.all()

for post in posts:
    if post.status == 'draft':
        post.status = 1  # DRAFT
    elif post.status == 'published':
        post.status = 2  # PUBLISHED
    post.save()

print("Valores de status corrigidos com sucesso.")
