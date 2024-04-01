from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .filters import PostFilter
from .models import Post
from .forms import PostForm


class NewsList(ListView):
    model = Post
    ordering = '-post_data_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsSearch(NewsList):
    template_name = 'search.html'

class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    slug = Post.post_type
    def get_type(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')