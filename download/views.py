from django.shortcuts import render
from pytubefix import YouTube, Playlist
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
            stream = youtube.streams.filter(progressive=True).get_highest_resolution()
            stream.download(ruta_descarga)
            mensaje = "¡Vídeo descargado correctamente!"
        except Exception:
            mensaje = "ingrese la url"

    return render(request, 'video.html', {'mensaje': mensaje})


def download_audio(request):
    mensaje = ""  
    if request.method == 'POST':
        enlace_video = request.POST['enlace_audio']
        ruta_descarga = 'audios/'  # Ajusta según tu configuración
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


def download_playlist(request):
    if request.method == 'POST':
        playlist_url = request.POST.get('enlace_playlist')
        ruta_descarga = 'playlist/' 
        
        try:
            # Crear objeto Playlist
            playlist = Playlist(playlist_url)
            
            # Recorrer cada video y descargar el stream progresivo más adecuado
            for video in playlist.videos:
                try:
                    # Obtener un stream progresivo con video y audio
                    stream = video.streams.filter(progressive=True).get_highest_resolution()
                    stream.download(ruta_descarga)  # Descargar el video
                except Exception as video_error:
                    print(f"Error al descargar el video {video.title}: {video_error}")
            
            # Mostrar el resultado en la página
            return render(request, 'video_playlist.html', {'mensaje': '¡Playlist descargada con éxito!'})

        except Exception as e:
            return render(request, 'video_playlist.html', {'mensaje': f"Error al procesar la playlist: {str(e)}"})

    return render(request, 'video_playlist.html')
