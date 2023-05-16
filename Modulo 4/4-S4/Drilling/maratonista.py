from persona import Persona

class Maratonista(Persona):
    movimiento = "trotando"
    
    def __init__(self, nombre):
        super().__init__(nombre)


