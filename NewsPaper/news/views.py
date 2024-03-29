from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = '-post_data_time'
    template_name = 'news.html'
    context_object_name = 'news'

class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
