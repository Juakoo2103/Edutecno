class CustomException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


def excepcion_propia():
    try:
        edad = int(input("ingrese edad para manejar excepciones: "))
        if edad < 0:
            raise CustomException("excepcioin propia ejecutada", 460)
        print(f'edad:  {edad}')
    except ValueError:
        print(f'Error : ingreso no valido')
    except CustomException as e:
        print(f'Error: {e.message}  - codigo {e.code} ')


excepcion_propia()
