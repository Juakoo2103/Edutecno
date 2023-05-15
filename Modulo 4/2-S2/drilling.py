class Persona:
    def __init__(self, nombre, apellido, genero, edad, estatura, peso):
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    @property  # get permite acceder al valor
    def nombre(self):
        return self._nombre

    @nombre.setter  # set permite setear un nuevo valor
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    def __str__(self):
        return f'Persona(nombre= {self.nombre}, apellido = {self.apellido}, genero = {self.genero}, edad = {self.edad}, estatura = {self.estatura}, peso = {self.peso})'


persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

print(
    f'el nombre de persona 1 es {persona_1.nombre} y su apellido es {persona_1.apellido}')

# Imprimimos persona a traves del metodo definido por __str__
print(persona_1)

persona_1.nombre = "Fulanito"  # Usando Setter
# Ejercicio drilling 1
print(persona_1.edad)  # Usando getter para mostrar valor anterior
persona_1.edad = 21  # Seteando un nuevo valor a traves del setter
print(persona_1.edad)  # Mostrando el nuevo valor seteado anteriormente
print("==================")

# Imprimimos persona a traves del metodo definido por __str__
print(persona_2)

# Ejercicio drilling 2
print(persona_2.apellido)  # Usando getter para mostrar valor anterior
persona_2.apellido = "Santiago"  # Seteando un nuevo valor a traves del setter
print(persona_2.apellido)  # Mostrando el nuevo valor seteado anteriormente
