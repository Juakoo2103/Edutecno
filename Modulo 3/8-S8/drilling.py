# Se solicita recorrer los datos numericos que se encuentran dentro de la siguiente lista de listas

lista_de_listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

for lista in lista_de_listas:
    if lista[0] == 0:
        continue
    for num in lista:
        if num == 0:
            continue
        print(num)

claves = ["A", "B", "C", "D"]
diccionario = zip(claves, lista_de_listas)
diccionario = dict(diccionario)
print(diccionario)
