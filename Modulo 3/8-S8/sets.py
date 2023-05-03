# Set, coleccion de datos, conjunto de datos se define utilizando la funcion set()
# se puede definir con {} pero se inicializa como un diccionario

# Definir un set
set_datos = set({10, 20, 15, 4, 3, 2})
my_set = {}  # se inicializa como un diccionario

# Verificar o ver el tipo de datos de un set
print("El tipo de dato de set_datos es:", type(set_datos))  # <class 'set'>
print("El tipo de dato de my_set es:", type(my_set))  # <class 'dict'>
print("=================================================")

# Verificar el largo de un set, longitud con len(params)
print("El largo de set_datos es:", len(set_datos))
print("El largo de my_set es:", len(my_set))
print("=================================================")

# Agregar elementos a un set
set_datos.add(15)
print(set_datos)
print("=================================================")

# Eliminar elementos de un set
set_datos.remove(15)
print(set_datos)
print("=================================================")

# Inicializar un set vacio
my_set = set()
my_set.add(2)
print(my_set)
print("=================================================")

# No permite elementos repetidos
set_datos.add(1)
print("set_datos", set_datos)
print("=================================================")

# Busqueda de elementos en un set
print("busqueda del numero 10 en set_datos", 10 in set_datos)
print("busqueda del numero 10 en set_datos", "python" in set_datos)
print("=================================================")

# Remover todos los elementos
my_set.clear()
print("my_set", my_set)
print("=================================================")

# del elimina el set desde su existencia
# del my_set
# print(my_set) my set is not define

# union() entrega un nuevo set de la union
my_set = (100, 200, 300)
new_set = set_datos.union(my_set)
print(new_set)
print("=================================================")

# actualizar un set, funcion update(set_a_agregar)
set_datos.update({10, 20, 30, 40, 50})
print("set datos", set_datos)
print("=================================================")

# Interseccion compara sets y entrega valores en común &
interseccion_set = new_set.intersection(my_set)
print("new_set: ", new_set)
print("my_set: ", my_set)
print("interseccion_set: ", interseccion_set)
print("=================================================")

# Diferencias compara sets y entrega sus valores diferentes ^
diferencias_set = new_set.difference(my_set)
print("new_set: ", new_set)
print("my_set: ", my_set)
print("diferencias_set: ", diferencias_set)
print("=================================================")

# Operatoria
a = {1, 2, 3, 4}
b = {2, 3, 4, 5, 6}
c = a & b
print(c)