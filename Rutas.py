import os
entrada = input("Introduc una ruta de archivos: \n")
ruta = os.path.isfile(entrada)

if ruta:
    print("El archivo existe.")
else:
    print("El archivo no existe")