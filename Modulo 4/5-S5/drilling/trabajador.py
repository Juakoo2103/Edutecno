from persona import Persona
from departamento import Departamento


class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, annio, nombre_depto, nombre_corto_dpto, salario):
        Persona.__init__(self, nombre, apellido, annio)
        Departamento.__init__(self, nombre_depto, nombre_corto_dpto)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario
