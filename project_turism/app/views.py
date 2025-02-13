from django.views.generic import ListView, CreateView
from rest_framework import viewsets
from rest_framework.reverse import reverse_lazy
from app.forms import PostForm
from app.models import Post
from app.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'postlist'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('index')