"""requerimos crear un registro de datos personales de tres personas.
los datos que se necesitan son: nombre , apellido y telefono.
Para ello, generamos un diccionario para cada una de las personas con los datos menccionados 
y luego los almacenaremos dentro de una lista. Finalmente, imprimiremos en pantalla la lista
"""

# los diccionarios, colecciones de datos formados por clave y valor

person1 = {
    "nombre": "Juan",
    "apellido": "Perez",
    "telefono": "123456789"
}

person2 = {
    "nombre": "Juan",
    "apellido": "Perez",
    "telefono": "123456789"
}

person3 = {
    "nombre": "Juan",
    "apellido": "Perez",
    "telefono": "123456789"
}

lista = [person1, person2, person3]

print(lista)

pacientes = {
    'paciente1': {'name': "Joaquin", 'edad': 75, 'peso': 75},
    'paciente2': {'name': "Ana", 'edad': 19, 'peso': 75},
    'paciente3': {'name': "Cristobal", 'edad': 21, 'peso': 75},
    'paciente4': {'name': "Luisa", 'edad': 22, 'peso': 75}
}

for key, value in pacientes.items():
    print(f"Paciente {key}:")
    print(
        f"Nombre: {value['name']}\nEdad: {value['edad']}\nPeso: {value['peso']}\n")
