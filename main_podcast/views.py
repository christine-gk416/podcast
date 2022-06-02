from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Post


class PodcastHome(ListView):
    template_name = "main_podcast/index.html"
    model = Post()


class PodcastDetails(DetailView):
    
    model = Post()


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'author', 'excerpt', 'content',
    'status', 'likes']


class PostEditView(UpdateView):
    model = Post
    fields = ['title', 'slug', 'author', 'excerpt', 'content',
    'status', 'likes']


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('index')