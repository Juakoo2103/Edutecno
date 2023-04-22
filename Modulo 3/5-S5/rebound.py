# Calcular factorial de un número

# variable que acumule el valor ingresado por el usuario
num = 0

# ciclo que sea positivo
while True:
    num = int(input("Ingrese un número entero positivo: "))
    if num > 0:
        break
    else:
        print("¡ALERT! tienes que ingresar un número positivo")

# El factorial de un número es la multiplicación de todos los números positivos del numero a uno

fact = 1
i = 1
while True:
    fact *= i
    i += 1
    if i > num:
        break
print(f"el factorial de {num} es {fact}")
