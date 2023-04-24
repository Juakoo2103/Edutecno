# eliminar letras de un string e imprimir en pantalla las consonantes restantes y su posicion dentro del string

palabra = "paralelepipedo"
vocales = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

for letra in palabra:
    if letra not in vocales:
        print(letra)

print("-------------------------------------------------------")

palabra = "paralelepipedo"
consonantes = ""

for i in range(len(palabra)):
    if palabra[i] not in vocales:
        consonantes += palabra[i]
        print(f"la latra {palabra[i]} se encuentra en la posicion {i}")

print("-------------------------------------------------------")
