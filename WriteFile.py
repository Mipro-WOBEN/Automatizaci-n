#with open('C:\Users\USUARIO\Desktop\pruebaspython\warhamer.txt', "r") as texto:
    #lectura = texto.readline()
#print(lectura)

def leer_archivo(nombre_archivo):
    try:
        # Intenta abrir el archivo en modo lectura
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        # Maneja el error si el archivo no se encuentra
        return "El archivo no se encuentra."
    except IOError:
        # Maneja otros errores de entrada/salida
        return "Ocurrió un error al leer el archivo."
    else:
        # Si no hubo errores, retorna el contenido
        return contenido

# Llama a la función y muestra el contenido
nombre_archivo = input("Ingrese el nombre del archivo a leer:")
contenido = leer_archivo(nombre_archivo)
print(contenido)
