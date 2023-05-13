from modelo.supervisor import Supervisor


class SupervisorService:
    def crear_supervisor(self):
        nombre = input('ingrese nombre del supervisor ')
        apellido = input('ingrese apellido del supervisor ')
        rut = input('ingrese rut del supervisor ')
        area = input('ingrese area del supervisor ')

        # para crear un supervisor se realiza una instancia de su constructor
        supervisor = Supervisor(nombre, apellido, rut, area)
        print("supervisor creado 👨‍🎓: ", supervisor)
