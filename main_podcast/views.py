from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class PodcastHome(TemplateView):
    template_name = "main_podcast/index.html"
