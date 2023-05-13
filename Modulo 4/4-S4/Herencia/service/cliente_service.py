from modelo.cliente import Cliente


class ClienteService:
    def crear_cliente(self):
        nombre = input('ingrese nombre del cliente ')
        apellido = input('ingrese apellido del cliente ')
        rut = input('ingrese rut del cliente ')
        descuento = input('ingrese descuento del cliente ')

        # para crear un supervisor se realiza una instancia de su constructor
        cliente = Cliente(nombre, apellido, rut, descuento)
        print("cliente creado😎: ", cliente)
