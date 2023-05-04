# Simula un juego de adivinanza,
# donde el jugador debe adivinar un numero aleatorio generado por el programa
# El programa le dara pistas al jugador sobre si el numero ingresado es mayor o menor que el numero generado
# y seguira pidiendo al jugador que ingrese un numero hasta que adivine correctamente
# import random

# numero_random = random.randint(0, 10)
# # print(numero_random)

# print("""Bienvenido al juego de adivinanzas,
# deberas adivinar un numero de 0 a 10 """)

# adivinanza = 11
# contador = 0
# while adivinanza != numero_random:
#     adivinanza = int(input("Ingresa un numero del 0 al 10: "))
#     contador += 1
#     if adivinanza > numero_random:
#         print("el numero es mayor al numero a adivinar")
#     elif adivinanza < numero_random:
#         print("el numero es menor al numero a adivinar")
#     else:
#         print(
#             f"Adivinaste! el numero era {numero_random} en , {contador} intentos")


# Se tiene el siguiente diccionario llamado ventas de una empresa que almacena las ventas
# mensuales deuna empresa por producto

# ventas = {
#     "producto_a": [100, 150, 200, 300, 250, 175, 125, 200, 300, 400, 500, 550],
#     "producto_b": [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325],
#     "producto_c": [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
# }

# # Calcular el total de ventas de cada producto

# dict_ventas = {}
# for producto, ventas_mensuales in ventas.items():
#     # total_ventas = sum(ventas_mensuales)
#     dict_ventas[producto] = sum(ventas_mensuales)
#     # print(f"Total de ventas de {producto}: {total_ventas}")
# print(dict_ventas)


# Se solicita crear un programa en Python que permita llevar el registro
# de los libros que han Sido prestados por una biblioteca.
# Para ello, se pide crear un conjunto (set) con los nombres de los libros
# prestados.
# A continuacion, se solicita imprimir en pantalla la cantidad total de libros
# prestados.
# Finalmente, se debe crear Otro conjunto con los nombres de los libros
# que han Sido devueltos y mostrar en pantalla los libros que aün no han Sido
# devueltos.
# libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del colera', 'La ciudad y los
# perros', 'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Paramo', 'La tregua'}

libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del colera', 'La ciudad y los perros',
                    'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Paramo', 'La tregua'}

libros_devueltos = {'Cien años de soledad',
                    'El otoño del patriarca', 'Rayuela'}
libros_sindevolver = libros_prestados.difference(libros_devueltos)
cantidad_libros = len(libros_sindevolver)

print("los nombres de los libros prestados son", libros_sindevolver)
print("los libros prestados son", cantidad_libros)
