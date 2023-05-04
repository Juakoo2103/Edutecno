# Crear una lista
my_list = [1, 2, 3, 4, 5]

# Agregar un elemento al final de la lista
my_list.append(6)

# Insertar un elemento en una posición específica
my_list.insert(3, 10)

# Acceder a un elemento por índice
first_element = my_list[0]
last_element = my_list[-1]

# Reemplazar un elemento por índice
my_list[1] = 20

# Eliminar un elemento por valor
my_list.remove(3)

# Eliminar y devolver el último elemento de la lista
last_element = my_list.pop()

# Obtener la longitud de la lista
length = len(my_list)

# Ordenar la lista de forma ascendente
my_list.sort()

# Ordenar la lista de forma descendente
my_list.sort(reverse=True)

# Obtener el índice de un elemento
index = my_list.index(4)

# Contar cuántas veces aparece un elemento en la lista
count = my_list.count(2)

# Extender la lista con otra lista o un objeto iterable
my_list.extend([7, 8, 9])

# Devolver una copia invertida de la lista
reversed_list = my_list[::-1]

# Devolver una copia superficial de la lista
copy_list = my_list.copy()

# Eliminar todos los elementos de la lista
my_list.clear()

# Crear una cadena a partir de los elementos de la lista, separados por un delimitador
my_list = ['a', 'b', 'c']
string = '-'.join(my_list)

# Crear una lista a partir de una cadena, utilizando un delimitador para separar los elementos
my_string = 'a-b-c'
my_list = my_string.split('-')

# Devolver el valor máximo de la lista
max_value = max(my_list)

# Devolver el valor mínimo de la lista
min_value = min(my_list)

# Devolver la suma de los valores de la lista
sum_value = sum(my_list)

# Devolver un objeto enumerado que contiene pares de índice-elemento
for index, element in enumerate(my_list):
    print(index, element)

# Devolver un objeto iterable que produce los elementos de la lista en orden inverso
for element in reversed(my_list):
    print(element)
