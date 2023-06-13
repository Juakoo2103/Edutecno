# REBOUND EXERCISES: AGREGANDO LÍNEAS AL ARCHIVO
# Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE:
# Apertura de archivos.EJERCICIO:Diseñe un programa en Pythonque agregueel siguiente contenido al archivo:
# informacion.dat.
# HolaMundo
# Esteenunanuevalíneaenelarchivo
# agregandolasegundalíneadelarchivo
# finalizandolalíneaagregada
from pathlib import Path

def agregar_info(texto):
    archivo = Path('Modulo 4/9-S9/rebound/rebound.dat')
    try:
        with open(archivo, 'a', encoding='utf-8') as file:
            file.write(texto+ '\n')

    except FileNotFoundError:
        print('Error: archivo no encontrado')
    except Exception as e:
        print('el error fue ', e)


agregar_info("Hola mundo")
# agregar_info("Este en una nueva línea en el archivo")
# agregar_info("agregando la segunda línea del archivo")
# agregar_info("finalizando la línea agregada")
