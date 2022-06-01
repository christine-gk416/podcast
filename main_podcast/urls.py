from django.urls import path

from .views import PodcastHome


urlpatterns = [
    path('', PodcastHome.as_view(), name='index'),
]