# numeros = [3, 5, 2, 8, 1, 10]

# # sumar todos los numeros de la lista utilizando while

# suma = 0
# recorrenum = 0

# while recorrenum < len(numeros):
#     suma += numeros[recorrenum]
#     recorrenum += 1

# print("La suma de los numeros en la lista es:", suma)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13, 14, 10, 11, 12, 13, 14, 10, 11, 12, 13, 14]
# menor = lista[0]
# mayor = lista[0]
# repetidos = lista[0]
# contador = 0
# listarepetidos = []

# for elemento in lista:
#     if elemento > mayor:
#         mayor = elemento
#     if elemento < menor:
#         menor = elemento
#     if elemento == repetidos and elemento not in listarepetidos:
#         listarepetidos.append(elemento)
#         contador += 1

# print(f"el elemento es mayor", mayor)
# print(f"el elemento es menor", menor)
# print(f"hay {contador} numeros repetidos ")
# print(f"el numero repetido es {listarepetidos}")


# de la siguiente lista de precios de productos


# calcular el precio total de la compra con uin descuento dle 10%

compra = [25.50, 12.30, 36.40, 9.75, 15.20]

comprdesc = sum(compra)*.90

print(f"su compra es {sum(compra)}")
print(f"y con el descuento del 10% queda el total de {comprdesc}")
