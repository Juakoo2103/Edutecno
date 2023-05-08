def es_palindromo(string):
    # Convertir la cadena a minúsculas y eliminar espacios en blanco
    string = string.lower().replace(" ", "")
    # Verificar si la cadena es un palíndromo
    if string == string[::-1]:
        print(
            f"La palabra que acabas de ingresar, '{string}', es un palíndromo.")
    else:
        print(
            f"La palabra que acabas de ingresar, '{string}', no es un palíndromo.")


# Pedir al usuario que ingrese una cadena
string = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")
# Verificar si la cadena es un palíndromo
es_palindromo(string)