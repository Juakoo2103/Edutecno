from trabajador import Trabajador
from persona import Persona
from departamento import Departamento
import pprint


def conocer_instancia(obj, compObj):
    respuesta = 'si' if isinstance(obj, compObj) else 'no'
    return respuesta


if __name__ == '__main__':
    trabajador = Trabajador('Juan', 'Perez', 2005,
                            'ingenieria de software', 'IS', 20000)
    pprint.pprint(trabajador.__dict__, width=1)


print('=========================')
print('trabajador es instancia de Persona ',
      conocer_instancia(trabajador, Persona))
print('=======================')
print('trabajador es instancia de departamento',
      conocer_instancia(trabajador, Departamento))
print('=======================')
print('trabajador es instancia de Trabajador',
      conocer_instancia(trabajador, Trabajador))
