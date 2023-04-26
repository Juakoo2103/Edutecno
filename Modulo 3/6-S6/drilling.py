# EJERCICIO
# Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
# orden de mayor a menor


# DESCOMENTAR PARA PROBAR
# primera forma no se si es la mas apropiada

# def ordenar_numeros(num1, num2, num3):
#     if num1 > num2:
#         if num1 > num3:
#             if num2 > num3:
#                 return [num1, num2, num3]
#             else:
#                 return [num1, num3, num2]
#         else:
#             return [num3, num1, num2]
#     else:
#         if num2 > num3:
#             if num1 > num3:
#                 return [num2, num1, num3]
#             else:
#                 return [num2, num3, num1]
#         else:
#             return [num3, num2, num1]


# # Solicitar al usuario que ingrese tres números diferentes
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# num3 = int(input("Ingrese el tercer número: "))

# # Llamar a la función y mostrar los números ordenados
# numeros_ordenados = ordenar_numeros(num1, num2, num3)
# print("Los números ordenados de mayor a menor son:", numeros_ordenados)


# segunda forma mas apropiada


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if len(set({num1, num2, num3})) != 3:
    print("debes ingresar tres números diferentes")
else:
    numeros_ordenados = sorted([num1, num2, num3], reverse=True)
    print("Los números ordenados de mayor a menor son:", numeros_ordenados)
