from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService


def main():
    # Creando instancias para acceder a los servicios
    menu_service = MenuService()
    cliente_service = ClienteService()
    supervisor_service = SupervisorService()

    while True:
        menu_service.imprimir_menu()  # Imprimiendo el menu a mostrar
        opcion = input('ingrese una opcion: ')
        match opcion:
            case "1":
                print('====================')
                cliente_service.crear_cliente()
                print('====================')
            case "2":
                print('====================')
                supervisor_service.crear_supervisor()
                print('====================')
            case "3":
                print('====================')
                print('Salimos 🚀')
                print('====================')
                break
            case _:
                print('====================')
                print('opcion no valida ❌')
                print('====================')


# funcion inicializadora para darle un punto de entrada/inicio al programa
if __name__ == "__main__":
    main()


# persona = Persona("fulanito","perez","1-9")
# print(persona)
# print(str(persona))
# persona.get_tipo()
# print("=============================")
# cliente = Cliente("fulanito","perez","1-9", "20")
# print(cliente)
# print(str(cliente))
# cliente.get_tipo()
# print("=============================")
# supervisor = Supervisor("fulanito","perez","1-9","Finanzas")
# print(supervisor)
# print(str(supervisor))
# supervisor.get_tipo()
# print("=============================")
