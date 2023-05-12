from personas import Persona


persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68.0)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75.0)

print(persona_1.get_edad())
print('========================================')
persona_1.set_edad(21)
print(persona_1.get_edad())
print('========================================')
print(persona_2.get_apellido())
print('========================================')
persona_2.set_apellido("Santiago")
print(persona_2.get_apellido())
