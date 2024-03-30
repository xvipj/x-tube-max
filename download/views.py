from django.shortcuts import render
from pytube import YouTube
import os
import moviepy.editor as mp

# Create your views here.
def download_video(request):
    mensaje = ""  
    if request.method == 'POST':
        enlace_video = request.POST['enlace_video']
        ruta_descarga = 'videos/'  # Ajusta según tu configuración
        try:
            youtube = YouTube(enlace_video)
            stream = youtube.streams.get_highest_resolution()
            stream.download(ruta_descarga)
            mensaje = "¡Vídeo descargado correctamente!"
        except Exception:
            mensaje = "ingrese la url"

    return render(request, 'video.html', {'mensaje': mensaje})


def download_audio(request):
    mensaje = ""  
    if request.method == 'POST':
        enlace_video = request.POST['enlace_audio']
        ruta_descarga = 'audio/'  # Ajusta según tu configuración
        try:
            # Descargar el video de YouTube
            youtube = YouTube(enlace_video)
            stream = youtube.streams.filter(only_audio=True).first() 
            video_path = stream.download(output_path=ruta_descarga)

            # Convertir el archivo de video a MP3
            audio_path = os.path.splitext(video_path)[0] + '.mp3'
            clip = mp.AudioFileClip(video_path)
            clip.write_audiofile(audio_path)
            clip.close()

            # Eliminar el archivo de video temporal
            os.remove(video_path)

            mensaje = "¡Audio descargado correctamente como MP3!"
        except Exception:
            mensaje = "Ingrese una URL válida"

    return render(request, 'audio.html', {'mensaje': mensaje})
