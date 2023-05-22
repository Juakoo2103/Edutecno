# EJERCICIO:
# Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el archivo,
# debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente creado.
# El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente:

# Datos de información en la línea 1
# Datos de información en la línea 2
# Datos de información en la línea 3
# Datos de información en la línea 4
# Datos de información en la línea 5

# Crear archivo y en caso de que existe lee la informacion
def crear_archivo():
    try:
        # Crea el archivo y se apertura
        file = open('informacion.dat', 'x', encoding='utf-8')
        file.close()  # Cierra el archivo
    except FileExistsError:
        print('El archivo ya existe, ha sido creado previamente')
        print('======== te entregare la informacion existente ========')
    except Exception as e:
        print(f'Error: {e}')


def leer():
    try:
        with open('informacion.dat', 'r', encoding='utf-8') as file:
            datos = file.readlines()
            for linea in datos:
                print(linea)
    except FileNotFoundError:
        print('el archivo no existe')


def escribir_archivo(lista):
    try:
        with open('informacion.dat', 'w', encoding='utf-8') as file:
            for dato in lista:
                file.write(dato+'\n')
    except FileNotFoundError:
        print('El archivo  no se encuentra')


lista = ["Datos de información en la línea 1",
         "Datos de información en la línea 2",
         "Datos de información en la línea 3",
         "Datos de información en la línea 4",
         "Datos de información en la línea 5"
         ]

crear_archivo()
leer()
escribir_archivo(lista)
