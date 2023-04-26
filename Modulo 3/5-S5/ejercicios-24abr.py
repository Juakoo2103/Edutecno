# La resistencia dentro de un circuito paralelo se calcula como:

# Rt= 1/((1/R1)+(1/R2)+(1/R3)+(1/Rn))

# Donde:

# RT es la resistencia total
# R1 es la resistencia 1
# R2 es la resistencia 2
# R3 es la resistencia 3
# Rn la n-esima resistencia

# Realiza el codigo en Pyuthon para calcular la resistencia total del circuito

# R1 = float(input("Ingrese la resistencia 1: "))
# R2 = float(input("Ingrese la resistencia 2: "))
# R3 = float(input("Ingrese la resistencia 3: "))

# r1 = abs(R1)
# r2 = abs(R2)
# r3 = abs(R3)

# print("aca con abs se pasa a valores absolutos")
# print(f"la resistencia de r1 es ", r1)
# print(f"la resistencia de r2 es ", r2)
# print(f"la resistencia de r3 es ", r3)
# Rt = 1/((1/r1)+(1/r2)+(1/r3))


# print("La resistencia total del circuito es: {:.2f}".format(Rt))

# print("======================================================================")


    while True:
        R1 = input("Ingrese la resistencia 1: ")
        if R1.isdigit():
            R1 = float(R1)
            r1 = abs(R1)
            break
        else:
            print("Error: Debe ingresar solo números. Intente de nuevo.")

    while True:
        R2 = input("Ingrese la resistencia 2: ")
        if R2.isdigit():
            R2 = float(R2)
            r2 = abs(R2)
            break
        else:
            print("Error: Debe ingresar solo números. Intente de nuevo.")

    while True:
        R3 = input("Ingrese la resistencia 3: ")
        if R3.isdigit():
            R3 = float(R3)
            r3 = abs(R3)
            break
        else:
            print("Error: Debe ingresar solo números. Intente de nuevo.")

    Rt = 1 / ((1/r1) + (1/r2) + (1/r3))

    print("La resistencia total del circuito es: {:.2f}".format(Rt))


# Realizar el calculo de la hipotenusa requiriendo el ingreso del cateto a y cateto b por parte del usuario en consola

# a = float(input("Ingrese el cateto a: "))
# b = float(input("Ingrese el cateto b: "))

# hipotenusa = (a**2 + b**2)**(1/2)

# print("la medida de la hipotenusa es: {:.2f}".format(hipotenusa))

# print("======================================================================")


# Pedir el ingreso de dos textos al usuario por consola y comparar si son iguales o del mismo tamaño

# texto1 = input("Ingrese el texto 1: ")
# texto2 = input("Ingrese el texto 2: ")
# if len(texto1) == len(texto2):
#     print("El texto 1 y el texto 2 en largo son del mismo tamaño")
# elif texto1 == texto2:
#     print("El texto 1 y el texto 2 son iguales")
# else:
#     print("El texto 1 y el texto 2 son diferentes")

# print("======================================================================")

# Simulaciön de una bomba de tiempo. Irå el tiempo desde el 5 al 1 en
# decremento. Al ejecutar el programa, se imprimirå el mensaje "Booom"

# import time

# i = 5

# while i > 0:
#     print(i)
#     time.sleep(1)
#     i -= 1

# print("Booom")

# print("======================================================================")


# Realizar la ejecucion de un menu utilizando el lenguaje python, donde se le indiquen varias opciones a seleccionar por el usuario y una opcion para salir del
# menu utulizar ciclos y estructuras condicionales

# mensaje = """ Menu principal

# [1] Entrar en menu principal

# [2] Novedades

# [3] Opciones

# [4] Salir """
# opcion = ""
# while opcion != "4":
#     print(mensaje)

#     opcion = input("Elija una opción: ")
#     if opcion == "1":
#         print("Entrando en menu principal")
#     elif opcion == "2":
#         print("Novedades")
#     elif opcion == "3":
#         print("Opciones")
#     elif opcion == "4":
#         print("Salir")
#     else:
#         print("Opción invalida")


# print("======================================================================")
