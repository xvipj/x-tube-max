from django.urls import path
from .views import download_video, download_audio, download_video_playlist, download_audio_playlist

urlpatterns = [
    path('', download_video, name="video"),
    path('audio/', download_audio, name="audio"),
    path('videoplaylist/', download_video_playlist, name="videoplaylist"),
    path('audioplaylist/', download_audio_playlist, name="audioplaylist"),
]
