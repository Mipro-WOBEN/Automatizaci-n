from moviepy.editor import VideoFileClip

def video_to_audio(video_file, audio_output):
    # Cargar el archivo de video
    video = VideoFileClip(video_file)
    
    # Extraer el audio del video
    audio = video.audio
    
    # Guardar el audio en el archivo de salida
    audio.write_audiofile(audio_output)
    
    # Cerrar el archivo de video y audio
    audio.close()
    video.close()

if __name__ == "__main__":
    # Especificar el archivo de video de entrada y el archivo de audio de salida
    video = input('Ingresa el nombre del video a convertir a audio1 \n')
    video_file = f"{video}.mp4"  # Cambia esto por el nombre de tu archivo de video
    audio  =input('Ingresa el nombre del audio convertido \n')
    audio_output = f"{audio}.mp3"  # Cambia esto por el nombre del archivo de salida de audio
    
    video_to_audio(video_file, audio_output)
    print(f"Audio extraído y guardado como {audio_output}")
