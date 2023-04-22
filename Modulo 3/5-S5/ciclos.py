# Los ciclos se ejecutan hasta que se cumple una condicion o se termine el ciclo completo

# ciclo for

""" numero = int(input('Ingrese un numero: '))

for i in range(1, numero):
    if i % 2 == 0:
        print(f'el numero {i} es par')
    elif i % 2 != 0:
        print(f'el numero {i} es impar')

print('----------------------------------------------------------------')


frutas = ['mango', 'banana', 'pera']

for fruta in frutas:
    print(fruta)

print('----------------------------------------------------------------')
"""

# while se evalua la condicion siempre True a menos que se cambie

i = 0
while i <= 10:
    i += 1
    print(f'imprimiendo el valor de {i}')


print('----------------------------------------------------------------')

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(f'ocupando continue {i}')

print('----------------------------------------------------------------')
