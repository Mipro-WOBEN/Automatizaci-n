import os
nombreArchivo = input('Ingresa el archivo con extensión para obtener ruta: ')
Archivo = os.path.join(os.getcwd(), f'{nombreArchivo}')

print(f'La ruta es: \n {Archivo}')