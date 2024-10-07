from cx_Freeze import setup, Executable

# Nombre de tu script de Python
script_name = input('Ingresa el archivo .py: ')

# Configuración de cx_Freeze
setup(
    name = "CrearArchivo",
    version = "0.1",
    description = "Crea archivos archivos con python",
    executables = [Executable(script_name)]
)
#python Ejec_Archivo.py build
#hacer excepción del archivo.exe en advance premium Security