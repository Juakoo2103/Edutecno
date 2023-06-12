# REBOUND EXERCISES: AGREGANDO LÍNEAS AL ARCHIVO
# Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE:
# Apertura de archivos.EJERCICIO:Diseñe un programa en Pythonque agregueel siguiente contenido al archivo:
# informacion.dat.
# HolaMundo
# Esteenunanuevalíneaenelarchivo
# agregandolasegundalíneadelarchivo
# finalizandolalíneaagregada


def agregar_info(texto):
    try:
        with open('9-S9/rebound/informacion.dat', 'w', encoding='utf-8') as file:
            file.write(texto+ '\n')
            file.close()

    except FileNotFoundError:
        print('Error: archivo no encontrado')
    except Exception as e:
        print('el error fue ', e)


agregar_info("Hola mundo")
agregar_info("Este en una nueva línea en el archivo")
agregar_info("agregando la segunda línea del archivo")
agregar_info("finalizando la línea agregada")
