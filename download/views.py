from django.shortcuts import render
from pytubefix import YouTube, Playlist
import os
from pathlib import Path
import moviepy.editor as mp

def download_video(request):
    mensaje = ""  
    load = False
    if request.method == 'POST':
        enlace_video = request.POST['enlace_video']
        ruta_descarga = str(Path.home() / "Downloads")
        try:
            load = True
            youtube = YouTube(enlace_video)
            stream = youtube.streams.filter(progressive=True).get_highest_resolution()
            stream.download(ruta_descarga)
            mensaje = "¡Vídeo descargado correctamente!"
            load = False
        except Exception:
            mensaje = "ingrese la url"

    return render(request, 'video.html', {'mensaje': mensaje, 'load': load})

def download_audio(request):
    mensaje = ""  
    if request.method == 'POST':
        enlace_video = request.POST['enlace_audio']
        ruta_descarga = str(Path.home() / "Downloads")
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


def download_video_playlist(request): 
    if request.method == 'POST':
        playlist_url = request.POST.get('enlace_playlist')
        ruta_descarga = str(Path.home() / "Downloads")
        
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

def download_audio_playlist(request):
    if request.method == 'POST':
        playlist_url = request.POST.get('enlace_playlist')
        # Obtener la ruta de la carpeta de descargas del sistema
        ruta_descarga = str(Path.home() / "Downloads")
        
        try:
            # Crear objeto Playlist
            playlist = Playlist(playlist_url)
            
            # Recorrer cada video y descargar el stream progresivo más adecuado
            for musica in playlist.videos:
                try:
                    # Obtener un stream progresivo con video y audio
                    stream = musica.streams.filter(progressive=True).get_highest_resolution()
                    video_path = stream.download(output_path=ruta_descarga)

                    # Convertir el archivo de video a MP3
                    audio_path = os.path.splitext(video_path)[0] + '.mp3'
                    clip = mp.AudioFileClip(video_path)
                    clip.write_audiofile(audio_path)
                    clip.close()

                    # Eliminar el archivo de video temporal
                    os.remove(video_path)
                except Exception as video_error:
                    print(f"Error al descargar el video {musica.title}: {video_error}")
            
            # Mostrar el resultado en la página
            return render(request, 'audios_playlist.html', {'mensaje': '¡Playlist descargada con éxito!'})

        except Exception as e:
            return render(request, 'audios_playlist.html', {'mensaje': f"Error al procesar la playlist: {str(e)}"})
    return render(request, 'audios_playlist.html')