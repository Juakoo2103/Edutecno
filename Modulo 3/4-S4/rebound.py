""" Requerimos crear una variable con el numero 8, una con el numero 10.5 y una con la palabra "ejercicio".
Luego crear un set que contendra cada una de las variables que creamos, y sera asignado a una variable.
A continuacion, creamos una lista que contendra el set creado anteriormente.
y una variable con el valor logico False.
Esta lista la asignaremos a una variable que luego imprimiremos en pantalla.
"""

#creacion de variables

variableUno = 8
variableDos = 10.5
variableTres = "ejercicio"

#creacion de set    

conjunto = set({variableUno, variableDos, variableTres})

print(conjunto)

#boolean

boleanoFalse = False

listaFalse = [boleanoFalse, conjunto]

print(listaFalse)

