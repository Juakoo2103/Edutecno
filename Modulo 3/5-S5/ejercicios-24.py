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

# Rt = 1/((1/R1)+(1/R2)+(1/R3))

# print("La resistencia total del circuito es: {:.2f}".format(Rt))

# print("======================================================================")


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

mensaje = """ Menu principal 

[1] Entrar en menu principal

[2] Novedades

[3] Opciones

[4] Salir """
opcion = ""
while opcion != "4":
    print(mensaje)

    opcion = input("Elija una opción: ")
    if opcion == "1":
        print("Entrando en menu principal")
    elif opcion == "2":
        print("Novedades")
    elif opcion == "3":
        print("Opciones")
    elif opcion == "4":
        print("Salir")
    else:
        print("Opción invalida")


print("======================================================================")
