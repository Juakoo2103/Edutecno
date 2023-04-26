# # REBOUND EXERCISES: CREACIÓN DE UN PROGRAMA CON TOMA DE DECISIONES
# CONDICIONALES.
# Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE:
# Sentencias condicionales.
# EJERCICIO
# Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
# En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
# subcondiciones; en su lugar, usar condiciones anidadas.

num = int(input("Ingrese un número: "))

if num == 0:
    print("El número es cero.")
else:
    if num > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")

    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
