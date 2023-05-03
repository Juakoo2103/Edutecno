# Eliminar los elementos duplicados
# Ordenar la lista resultante en orden ascendente

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

lista_nueva = []

for i in mi_lista:
    if i not in lista_nueva:
        lista_nueva.append(i)
lista_nueva.sort()
print(lista_nueva)
