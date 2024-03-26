from django.urls import path
from .views import download_video, download_audio

urlpatterns = [
    path('', download_video, name="video"),
    path('audio/', download_audio, name="audio"),
]
