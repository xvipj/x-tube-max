from django.urls import path
from .views import download_video, download_audio, download_playlist

urlpatterns = [
    path('', download_video, name="video"),
    path('audio/', download_audio, name="audio"),
    path('videoplaylist/', download_playlist, name="videoplaylist"),
]
