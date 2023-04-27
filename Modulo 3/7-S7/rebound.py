# recorrer y ver si son par impar o 0

numeros = [1, 20, 33, 41, 54, 67, 709, 78, 69, 150]

for num in numeros:
    if num == 0:
        print(num, "es 0")
    elif num % 2 == 0:
        print(num, "es par")
    else:
        print(num, "es impar")
