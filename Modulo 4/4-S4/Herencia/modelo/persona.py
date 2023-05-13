class Persona:
    def __init__(self, nombre, apellido, rut):
        self._nombre = nombre
        self._apellido = apellido
        self._rut = rut

    # getters y setter pythonic amente hablando

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self.apellido = apellido

    @property
    def rut(self):
        return self._rut

    @rut.setter
    def rut(self, rut):
        self.rut = rut

    # function o method
    def get_tipo(self):
        print(f"soy del tipo {self}")
        print(type(self))
    # function para imprimir el objeto en string
    def __str__(self):
        return f'Persona(nombre= {self._nombre}, apellido = {self._apellido}, rut = {self._rut})'



# persona_1 = Persona("Fulanito", "Perez", "1-9")
# print(persona_1.nombre)
