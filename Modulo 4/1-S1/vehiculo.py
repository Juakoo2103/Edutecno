class Vehiculo:
    # constructor con parametros para realizar una instancia de la clase vehiculo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto


# creando una instancia de la clase vehiculo
vehiculoUno = Vehiculo("Mazda", "Blanco", "CX-5", 2000, 2.5, 2.0)
# imprimiendo los datos del vechiculo creado
print(vehiculoUno.marca, vehiculoUno.color, vehiculoUno.modelo)

# se puede cambiar el valor de un objeto acediendo a el y poniendo el nuevo estado
vehiculoUno.color = "Negro"
print(vehiculoUno.color)
