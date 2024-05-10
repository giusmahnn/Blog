from django.views.generic import (ListView,
                                TemplateView,
                                DetailView,
                                CreateView, 
                                UpdateView,
                                DeleteView)
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogPageView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post')