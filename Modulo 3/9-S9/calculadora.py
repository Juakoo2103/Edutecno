# Se pide realizar una calculadora declarando funciones para cada tipo de calculo que se realice

# realizar un menu con opciones para seleccionar que calculo se desea realizar

# el ingreso es por consola, requerir al usuario la opcion y numeros al que se realizara el calculo

# verificar errores de ingreso

# verificar division por cero


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


def opciones():
    print("bienvenidos a la calculadora")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Division")
    print("5.- Salir")
    print("ingrese una opcion : ")


def calculadora():
    while True:
        try:
            opciones()

            opcion = input("1/2/3/4/5: ")
            a = float(input("Ingrese el primer numero:"))
            b = float(input("Ingrese el segundo numero:"))

            # Evaluar la opcion y seleccionar la funcion

            match opcion:
                case '1':
                    resultado = suma(a, b)
                case '2':
                    resultado = resta(a, b)
                case '3':
                    resultado = multi(a, b)
                case '4':
                    resultado = dividir(a, b)
                case '5':
                    print("gracias por usar la calculadora vuelva pronto")
                    break
                case '6':
                    print("opcion no valida,elija una opcion valida")
            if resultado is not None:
                print("=======================================================")
                print(
                    f"|||            el resultado es {resultado           }            |||")
                print("=======================================================")
                break
        except Exception as e:
            print("Error", e)


calculadora()
