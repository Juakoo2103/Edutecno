# Se tiene una lista de nombres de personas
# imprimir los nombres que tienen una longitud mayor que 5 caracteres

# nombres = ["Juan", "Maria", "Pedro", "Ana", "Roberto", "Lucia", "Luisa"]

# for nombre in nombres:
#     if len(nombre) > 5:
#         print(nombre)

# Crear una lista de numeros donde cada numero es la longitud de una palabra

# animales = ["gato", "perro", "elefante", "jirafa", "tigre"]

# largo = []
# for animal in animales:
#     len(animal)
#     largo.append(len(animal))
# print(largo)


# Solicita al usauario ingresar un password hasta que el password coincida con el password predefinido

# password = "contra"

# while True:
#     pw = input("ingresa la clave: ")
#     if password.lower() == pw.lower():
#         print("acceso concedido")
#         break
#     else:
#         print("ingresa otra contraseña")


# password = "pass"
# solicitud_clave = input("Ingrese su clave ")
# intentos = 0

# while password != solicitud_clave:
#     print("la clave no coincide")
#     solicitud_clave = input("Ingrese su clave ")
# print("Bienvenido!")

# Simula un programa que permite a los usuarios adivinar una palabra secreta

# palabra_secreta = "python"


# def comprobar_adivinanza(palabra, adivinanza):
#     letras_correctas = 0
#     for letra in adivinanza:
#         if letra in palabra:
#             letras_correctas += 1
#     return letras_correctas


# while True:
#     adivinanza = input("adivina la palabra secreta: ")
#     letras_correctas = comprobar_adivinanza(palabra_secreta, adivinanza)
#     if letras_correctas == len(palabra_secreta):
#         print("adivinaste la palabra")
#         break
#     else:
#         print("solo adivinaste", letras_correctas, " letras")

import random
palabras_secretas = ["arroz", "pollo", "pure", "choclo", "chorrillana"]

adivinanza = random.choice(palabras_secretas)
intentos = 5
turno = 0
ingreso = ""
while adivinanza != ingreso and turno < intentos:
    ingreso = input("ingresa la palabra para adivinar :")
    turno += 1
    if ingreso.lower() == adivinanza.lower():
        print(f"adivinaste! en  {turno} turno")
    elif turno == intentos:
        print(
            f"no has adivinado y ya no te quedan mas intentos la palabra era {adivinanza}")
    else:
        print(f"sigue intentando, vas en el turno {turno}/5 ")
