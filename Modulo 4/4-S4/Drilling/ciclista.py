from persona import Persona

class Ciclista(Persona):
    movimiento = "rodando"

    def __init__(self, nombre):
        super().__init__(nombre)
