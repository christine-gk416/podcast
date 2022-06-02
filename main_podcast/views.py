from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Post


class PodcastHome(ListView):
    template_name = "main_podcast/index.html"
    model = Post()
