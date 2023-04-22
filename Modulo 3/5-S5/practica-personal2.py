"""Práctica Control de Flujo 3

Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.
Evalúa a un candidato que sabe inglés, pero no programa en Python."""

sabes_ingles = input("Sabes Ingles (Sí/No): ").lower() == "sí"
sabes_python = input("Sabes Python (Sí/No): ").lower() == "sí"
