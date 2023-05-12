from multipledispatch import dispatch


class Persona:
    @dispatch(str, str, str, int, float, float)
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad

    def get_estatura(self):
        return self.estatura

    def get_peso(self):
        return self.peso

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def set_estatura(self, estatura):
        self.estatura = estatura

    def set_peso(self, peso):
        self.peso = peso

