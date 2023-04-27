# def resistencia_correcta(i):

#     while True:
#         try:
#             r = input(i)
#             if r.isdigit():
#                 r = float(r)
#                 r = abs(r)
#                 return r
#             else:
#                 print("ha ingresado un valor que no es digito")
#         except Exception as e:
#             print("Error: Debe ingresar solo números. Intente de nuevo.", e)


# r_1 = resistencia_correcta("Ingrese la resistencia 1: ")
# r_2 = resistencia_correcta("Ingrese la resistencia 2: ")
# r_3 = resistencia_correcta("Ingrese la resistencia 3: ")

# Rt = 1 / ((1/r_1) + (1/r_2) + (1/r_3))

# print("La resistencia total del circuito es: {:.2f}".format(Rt))


# while True:
#     R1 = input("Ingrese la resistencia 1: ")
#     if R1.isdigit():
#         R1 = float(R1)
#         r1 = abs(R1)
#         break
#     else:
#         print("Error: Debe ingresar solo números. Intente de nuevo.")

# while True:
#     R2 = input("Ingrese la resistencia 2: ")
#     if R2.isdigit():
#         R2 = float(R2)
#         r2 = abs(R2)
#         break
#     else:
#         print("Error: Debe ingresar solo números. Intente de nuevo.")

# while True:
#     R3 = input("Ingrese la resistencia 3: ")
#     if R3.isdigit():
#         R3 = float(R3)
#         r3 = abs(R3)
#         break
#     else:
#         print("Error: Debe ingresar solo números. Intente de nuevo.")

# Rt = 1 / ((1/r1) + (1/r2) + (1/r3))

# print("La resistencia total del circuito es: {:.2f}".format(Rt))


def calculadoraResist(i):
    while True:
        try:
            r = float(input(i))
            if r > 0:
                abs(r)
                return r
            else:
                print("el valor es menor a 0")
        except Exception as e:
            print("Ha ocurrido un error", e)


r_1 = calculadoraResist("Ingrese la resistencia 1: ")
r_2 = calculadoraResist("Ingrese la resistencia 2: ")
r_3 = calculadoraResist("Ingrese la resistencia 3: ")

Rt = 1 / ((1/r_1) + (1/r_2) + (1/r_3))

print("La resistencia total del circuito es: {:.2f}".format(Rt))
