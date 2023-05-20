from modelo.cliente import Cliente


class ClienteService:
    def __init__(self):
        # ClienteService tiene una lista de clientes como propiedad
        # Se carga la lista de clientes cuando se instancia ClienteService
        self._clientes = self.load_clientes()

    # carga de clientes a traves de archivo, lectura y creacion si el archivo no existe

    def load_clientes(self):
        try:
            # with sirve para abrir y cerrar el archivo es como un loop de abre y cierre mientras se capturan los datos que necesito
            with open('cliente.txt', 'r') as file:
                # retorna una lista de tipo str con todas las lineas que leyo
                clientes = file.readlines()
        except FileNotFoundError:  # Si ocurre el error de archivo no existe se procede a crearlo
            clientes = []
            with open('cliente.txt', 'w') as file:
                file.writelines(clientes)  # crea el archivo si no existe
        return clientes

    # Guardado de archivo, escritura sobre el archivo
    def save_clientes(self):
        with open('cliente.txt', 'w') as file:
            for cliente in self._clientes:  # se recorre la lista existente de clientes
                # se va escribiendo en el archivo cliente.txt cada nuevo cliente
                file.write(str(cliente))

    def crear_cliente(self):
        # (self, nombre, apellido, rut, descuento)
        nombre = input('Ingrese el nombre del cliente: ')
        apellido = input('Ingrese el apellido del cliente: ')
        rut = input('Ingrese el rut del cliente: ')
        descuento = input('Ingrese el descuento del cliente: ')

        # instanciar un cliente
        cliente = Cliente(nombre, apellido, rut, descuento)
        print(f'Cliente creado: {cliente}')

        # agregar cliente a lista clientes existentes
        self._clientes.append(cliente)

        # guardar los clientes
        self.save_clientes()

    def list_clientes(self):
        print('lista de clientes')
        for cliente in self._clientes:
            print(cliente)
