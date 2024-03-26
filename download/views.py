from django.shortcuts import render
from pytube import YouTube

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
            youtube = YouTube(enlace_video)
            stream = youtube.streams.filter(only_audio=True).first() 
            stream.download(ruta_descarga)
            mensaje = "¡Audio descargado correctamente!"
        except Exception:
            mensaje = "Ingrese una URL válida"

    return render(request, 'audio.html', {'mensaje': mensaje})
