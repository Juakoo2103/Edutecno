# diccionarios , colecciones estructuradas en clave : valor clave como key valor como value
# van estructurados entre llaves {} como uin objeto JSON
# se puede definir usando dict()
# se puede definir usando {} llaves

# Creando un diccionario o instanciando un diccionario
my_dict = dict()
other_dict = {}

# se puede saber el tipo con type()
print("El tipo de diccionario es: ", type(my_dict))

other_dict = {
    # clave : valor
    'Nombre': 'Maria',
    'Apellido': "Perez",
    'Edad': 25,
    'Direccion': 'Curico 1320'

}

my_dict = {
    'Nombre': 'Maria',
    'Apellido': "Perez",
    'Edad': 25,
    'Direccion': {
        'Region':   'IV Region',
        'Calle':   'Almirante Pastene',
        'Numero':   '1320',
        'Codigo Postal':   '1122333'
    }

}

print("other_dict", other_dict)
print("my_dict", my_dict)
print("================================================================================================")

# Busqueda mediante una clave, nombre_Diccionario[clave]

print("Nombre: ", my_dict['Nombre'])
# Respeta las mayuscula para la busqueda de claves
# print("Nombre: ", my_dict['nombre'])
print("================================================================================================")

print("apellido se encuentra dentro del diccionaio my_dict : ",
      'Apellido' in my_dict)  # Retorna True or False si existe o no la clave
print("================================================================================================")

print("Perez se encuentra en el diccionario con key 'Apellido' : ",
      'Perez' in my_dict['Apellido'])
print("================================================================================================")


# eliminar un elemento dentro de un diccionario, del nombre_diccionario['clave']

print("other_dict", other_dict)
del other_dict['Edad']
print("other_dict elminado edad ", other_dict)
print("================================================================================================")


claves = ["a", "b", "c"]
valores = [1, 2, 3]

nuevo_diccionario = {}
for i in range(len(claves)):
    nuevo_diccionario[claves[i]] = valores[i]

print(nuevo_diccionario)