import os

def buscar_archivo(directorio, nombre_archivo):
    archivos_encontrados = []
    for ruta, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo == nombre_archivo:
                archivos_encontrados.append(os.path.join(ruta, archivo))
    return archivos_encontrados

# Solicita al usuario que ingrese el nombre del archivo a buscar
nombre_archivo = input("Ingrese el nombre del archivo a buscar (con extensión): ")

# Solicita al usuario que ingrese el directorio en el cual buscar
directorio_busqueda = input("Ingrese el directorio donde buscar: ")

# Verifica si el directorio existe
if not os.path.isdir(directorio_busqueda):
    print("El directorio especificado no existe.")
else:
    # Busca el archivo
    archivos = buscar_archivo(directorio_busqueda, nombre_archivo)

    # Imprime los archivos encontrados
    if archivos:
        print("Archivos encontrados:")
        for archivo in archivos:
            print(archivo)
    else:
        print("No se encontraron archivos con ese nombre.")
