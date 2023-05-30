class Adulto(Exception):
    def __init__(self, message):
        self.message = message


class Menor(Exception):
    def __init__(self, message):
        self.message = message


def adulto_menor():
    while True:
        try:
            edad = int(input("ingrese edad para manejar excepciones: "))
            if edad >= 18:
                raise Adulto("La persona es adulta")
            else:
                raise Menor("La persona no es adulta")
        except ValueError:
            print(f'Error : ingreso no valido')
        except Adulto as e:
            print(f'{e.message}')
        except Menor as e:
            print(f'{e.message}')


adulto_menor()
