# Se solicita crear un programa en Python que permita Ilevar el registro de los invitados
# a una fiesta.
# Para ello, se pide crear dos conjuntos (set): uno con los nombres de los invitados
# confirmados y Otro con los nombres de los invitados que han Ilegado a la fiesta.
# A medida que los invitados van Ilegando a la fiesta, se deben ir agregando sus
# nombres al conjunto de los que asistieron.
# Ademås, se debe imprimir en pantalla la cantidad de invitados confirmados y la
# cantidad de invitados que han asistido.
# Finalmente, se debe imprimir en pantalla el nombre de los invitados que confirmaron
# su asistencia pero aün no han Ilegado a la fiesta, es decir, los nombres que se
# encuentran en el conjunto de confirmados pero no en el conjunto de los que
# asistieron.

# UNA FORMA
# invitados = {"maria", "sofia", "ernesto"}
# llegaron = set()
# while len(invitados ^ llegaron) >= 0:
#     opciones = input('''FIESTA DEL SIGLO Consultar quienes han llegado (c)
#     Agregar un invitado que ha llegado (a)
#     Salir (s) ''').lower().strip()
#     faltan_por_llegar = invitados ^ llegaron
#     match opciones:
#         case "c" | "consultar":
#             print(f'La cantidad de invitados que llegaron es {len(llegaron)}')
#             print(f'Falta por llegar {faltan_por_llegar}')
#         case "a" | "agregar":
#             nuevo = input('Ingresa nombre de quien ha llegado ')
#             if nuevo in invitados:
#                 llegaron.add(nuevo)
#             else:
#                 print("invitado no registrado, ingrese otro")
#             print(f' los invitados que han llegado son {llegaron}')
#         case "s" | "salir": print("Adios")
#     break
# else:
#     print("llegaron todos los invitados, exito!")


