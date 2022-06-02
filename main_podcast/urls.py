from django.urls import path

from .views import PodcastHome
from .models import Post


urlpatterns = [
    path('', PodcastHome.as_view(model=Post), name='index'),
]