# EJERCICIO
# Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
# 1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
# Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
# • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista.
# • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.

lista_de_listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

for lista in lista_de_listas:
    if lista[0] == 0:
        continue
    for num in lista:
        if num == 0:
            continue
        print(num)


list_of_list = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
list_without_zeros = list(filter(lambda x: x[0] != 0, list_of_list))
final_list = list(filter(lambda x: x != 0, [
    item for sublist in list_without_zeros for item in sublist]))
print(final_list)
