from django.urls import path

from .views import PodcastHome, PostCreateView, PodcastDetails, PostEditView, PostDeleteView
from .models import Post


urlpatterns = [
    path('', PodcastHome.as_view(model=Post), name='index'),
    path('post-form/', PostCreateView.as_view(model=Post), name='create-post'),
    path('edit-form/<slug:slug>/', PostEditView.as_view(model=Post), name='edit-post'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(model=Post), name='delete'),
    path('post/<slug:slug>/', PodcastDetails.as_view(model=Post), name='post_detail'),
    
]
