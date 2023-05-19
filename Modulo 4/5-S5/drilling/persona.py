class Persona:
    # constructor con parametros
    def __init__(self, nombre, apellido, anio):
        self.__nombre = nombre
        self.__apellido = apellido 
        self.__anio = anio 
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre 

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido 
    
    @property
    def anio(self):
        return self.__anio
    
    @anio.setter
    def anio(self, anio):
        self.__anio = anio 


