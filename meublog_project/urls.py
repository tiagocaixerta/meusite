from django.contrib import admin
from django.urls import path
from blog.views import PostView, PostDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='home'),  # Página inicial do blog
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),  # Detalhes do post
]
