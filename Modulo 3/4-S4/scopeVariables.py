#scope o alcance de una variable

#alcance global o alcance local

#scope global
variable_global = "se accede desde todo el documento"

#scope local
#se define como un metodo

def suma(a,b):
    suma_valores = a+b
    return suma_valores
print(suma(10,20))
print(variable_global)
