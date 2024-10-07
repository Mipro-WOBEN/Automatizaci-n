def escribir_en_archivo(nombre_archivo, modo='w'):
    print("Ingrese las líneas que desea escribir en el archivo. Ingrese 'FIN' para terminar.")

    lineas = []
    while True:
        linea = input()
        if linea == 'FIN':
            break
        lineas.append(linea + '\n')

    try:
        with open(nombre_archivo, modo) as archivo:
            archivo.writelines(lineas)
        print(f"Contenido escrito en {nombre_archivo} exitosamente.")
    except IOError as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")

# Solicita al usuario que ingrese el nombre del archivo y el modo de apertura
nombre_archivo = input("Ingrese el nombre del archivo (con extensión): ")
modo = input("Ingrese el modo de apertura ('w' para sobrescribir, 'a' para añadir): ")

# Llamar a la función para escribir en el archivo
escribir_en_archivo(nombre_archivo, modo)
