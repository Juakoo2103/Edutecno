class Rango(Exception):
    def __init__(self, message):
        self.message = message


def rango_salario():
    while True:
        try:
            salario = int(input("Ingrese el salario : "))
            if salario < 1000 or salario > 2000:
                raise Rango("Salario no esta definido en el rango de 1000 a 2000")
        except ValueError:
            print(f'Error : ingreso no valido')
        except Rango as e:
            print(f'{e.message}')


rango_salario()
