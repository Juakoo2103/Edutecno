class Departamento:
    def __init__(self, nombre_depto, nombre_corto_depto):
        self.__nombre_depto = nombre_depto
        self.__nombre_corto_depto = nombre_corto_depto

    @property
    def nombre_depto(self):
        return self.__nombre_depto

    @nombre_depto.setter
    def nombre_depto(self, nombre_depto):
        self.__nombre_depto = nombre_depto

    @property
    def nombre_corto_depto(self):
        return self.__nombre_corto_depto

    @nombre_corto_depto.setter
    def nombre_corto_depto(self, nombre_corto_depto):
        self.__nombre_corto_depto = nombre_corto_depto

