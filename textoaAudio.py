from gtts import gTTS
import os

def texto_a_audio(texto, nombre_archivo):
    try:
        tts = gTTS(text=texto, lang='es')
        tts.save(nombre_archivo)
        print(f"El archivo de audio se ha guardado como {nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al convertir el texto a audio: {e}")

# Solicita al usuario que ingrese el texto
texto = input("Ingrese el texto que desea convertir a audio: ")

# Solicita al usuario que ingrese el nombre del archivo de salida
nombre_archivo = input("Ingrese el nombre del archivo de salida (con extensión .mp3): ")

# Llamar a la función para convertir el texto a audio
texto_a_audio(texto, nombre_archivo)

