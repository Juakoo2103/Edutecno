# Las excepciones pueden ocurrir en el momento de transformacion, asignacion, evaluacion de variables.

try:
    num1 = int(input("ingresa un numero: "))
    num2 = int(input("ingresa un numero: "))
    if num2 == 0:
        raise ZeroDivisionError("no se puede dividir por 0")
    division = num1 / num2
    print(division)


except ZeroDivisionError as e:
    print(e)
