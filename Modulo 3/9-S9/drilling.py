# CUE: FUNCIONES EN PYTHONDRILLING:
# TRABAJANDO EN FUNCIONESPara resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del
# CUE:Funciones en Python.EJERCICIOCrear una función que sume dos números, otra que reste dos números,
# otra que multiplique dos números, y  otra  que  divida  dos  números.  Adicionalmente, crear  una
# función  que  acepte  dos números  como  parámetros  y  regrese  el  resultado  en  forma  de tupla  de  su  suma,
# resta, multiplicación y división.Los  resultados  se  deben  almacenar  en  un  diccionario, cuyas  claves
# serán:  Suma,  Resta, Multiplicación y División, y los valores de cada clave serán los resultados obtenidos
# con la función creada anteriormente.

def suma(num1, num2):
    sumatoria = num1 + num2
    return sumatoria


def resta(num1: float, num2: float):
    resto = num1 - num2
    return resto


def multi(num1, num2) -> float:
    multiplica = num1 * num2
    return multiplica


def dividir(num1, num2):
    # div = num1 / num2
    # return div
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("No se puede dividir entre cero")


def operaciones(a, b):
    return (suma(a, b),
            resta(a, b),
            multi(a, b),
            dividir(a, b))


resultado = operaciones(2, 3)
print(resultado)
diccionario = {
    'Suma': resultado[0],
    'Resta': resultado[1],
    'Multi': resultado[2],
    'Dividir': resultado[3],
}

print(diccionario)
