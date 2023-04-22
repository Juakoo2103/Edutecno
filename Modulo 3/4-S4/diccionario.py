#creando dicccionario 

estudiantes = {
    #clave:valor
    "Juan":20,
    "Pedro":10,
    "Maria":30,
    "Ana":15,
    "Joseph": 29
}

print(estudiantes) #{"Juan":20,"Pedro":10,"Maria":30,"Ana":15,"Joseph":29}

print(estudiantes["Juan"]) #20
print(estudiantes["Pedro"]) #10
print(estudiantes["Maria"]) #30
print(estudiantes["Ana"]) #15
print(estudiantes["Joseph"]) #29

del estudiantes["Ana"]

print(estudiantes) #{"Juan":20,"Pedro":10,"Maria":30,"Joseph":29}

#obterner las claves de un diccionario
claves = estudiantes.keys()
print(claves) #["Juan","Pedro","Maria","Ana","Jose

pacientes = {
    'Joaquin': {'edad': 75, 'peso': 75},
    'Maria': {'edad': 19, 'peso': 75},
    'Pedro': {'edad': 21, 'peso': 75},
    'Ana': {'edad': 22, 'peso': 75}
}

print(pacientes) #{'Joaquin': {'edad': 25, 'peso': 75}, 'Maria': {'edad': 25, 'peso': 75}, 'Pedro': {'edad': 25, 'peso': 75}, 'Ana': {'edad': 25, 'peso': 75}}

edadPaciente1 = pacientes['Ana']['edad']
edadPaciente2 = pacientes['Joaquin']['edad']
edadPaciente3 = pacientes['Pedro']['edad']


print(f'la edad de Ana es {edadPaciente1}') #25
print(f'la edad de Joaquin es {edadPaciente2}')
print(f'la edad de Pedro es {edadPaciente3}') #25


