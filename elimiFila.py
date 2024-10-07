import os

def eliminar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
        print(f"El archivo {nombre_archivo} ha sido eliminado exitosamente.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except PermissionError:
        print(f"No tienes permiso para eliminar el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el archivo: {e}")

# Solicita al usuario que ingrese el nombre del archivo a eliminar
nombre_archivo = input("Ingrese el nombre del archivo a eliminar (con ruta si es necesario): ")

# Llamar a la función para eliminar el archivo
eliminar_archivo(nombre_archivo)
