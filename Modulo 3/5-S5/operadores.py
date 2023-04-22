# operadores logicos
# and or not
# Evaluar booleanos

a = True
b = False

print(a and b)  # False , se deben cumplir ambas condiciones
print(a or b)  # True, se deben cumplir una de las dos condiciones

print(not a)  # False, se cambia el valor de la condicion
print(not b)  # True, se cambia el valor de la condicion

print(not (a or b))  # False
print(not (a and b))  # True

# Operadores de comparacion
# <, <=, >, >=, ==,!=,

c = "10"
d = "5"

print(c > d)  # True
print(c < d)  # False
print(c >= d)  # True
print(c <= d)  # False
print(c == d)  # False
print(c != d)  # True

e = "Hola"
f = "Paralelepipedo"

print(e == f)
print(len(e) > len(f))
print(e != f)
