# EJERCICIOS:Realiza los pasos que se exponen a continuación:
# 1.-Se da el siguiente diccionario:
# usuarios={'001':'Marca','002':'Mónica','003':'Jacob'}
# 2.-Intente imprimir el valor de la clave: id_usuario='004'
# 3.-En caso de KeyError, imprima en la consola el siguiente 
# mensaje:'La clave 004 no está en el diccionario. Añadiendo clave...'4.-
# Luego, agregue esta clave al diccionario con el valor “Ninguno”, 
# e imprima el diccionario de usuarios en la consola.
# Partiendo del siguiente código en Python: usuarios={'001':'Mark','002':'Monica','003':'Jacob'}
# id_usuario='004'

import pprint

usuarios = {'001':'Marca','002':'Mónica','003':'Jacob'}
mensaje = 'La clave 004 no está en el diccionario'
id_usuario = '004'

try:
    print(usuarios[id_usuario])
except KeyError:
    print(mensaje)
    usuarios[id_usuario] = None

pprint.pprint(usuarios, width=1)

