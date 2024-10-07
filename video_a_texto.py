import moviepy.editor as mp
import speech_recognition as sr
import os

# Ruta del video y del archivo de audio
video_path = input("Ingresa el archivo .mp4 a transcribir: ")
audio_path = "temp_audio.wav"

# Extraer el audio del video utilizando moviepy
video = mp.VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Función para transcribir audio en segmentos de 1 minuto
def transcribe_audio(audio_path):
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="es-ES")
            return text
        except sr.UnknownValueError:
            return "Google Web Speech no pudo entender el audio"
        except sr.RequestError as e:
            return f"Error al solicitar resultados de Google Web Speech; {e}"

# Segmentar y transcribir el audio si es necesario
audio_duration = video.audio.duration  # Duración del audio en segundos
segment_duration = 60  # Duración del segmento en segundos
transcript = ""

if audio_duration > segment_duration:
    for i in range(0, int(audio_duration), segment_duration):
        segment_audio_path = f"temp_audio_segment_{i}.wav"
        video.audio.subclip(i, min(i + segment_duration, audio_duration)).write_audiofile(segment_audio_path)
        transcript += transcribe_audio(segment_audio_path) + " "
        os.remove(segment_audio_path)
else:
    transcript = transcribe_audio(audio_path)

# Imprimir la transcripción
print("Transcript: " + transcript)

# Eliminar el archivo de audio temporal
os.remove(audio_path)

