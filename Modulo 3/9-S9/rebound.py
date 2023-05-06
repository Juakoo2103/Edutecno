# Crear  una  función  que  acepte  3  números  como parámetros,
# sume  todos  los  valores,  y adicionalmente reste el segundo y tercer parámetro al primero.
# Al invocar la función, debemos pasarle los parámetros en forma de lista.
# Esta devolverá ambos resultados en una tupla. Los resultados se deben imprimir en pantalla

def funcion_rara(a, b, c):
    suma = a+b+c
    difsum = a - (b+c)
    return (suma, difsum)


listanum = [1, 2, 3]

funcion_rara(*listanum)  # xargs se le pasan los parametros que hay

print(funcion_rara(*listanum))
