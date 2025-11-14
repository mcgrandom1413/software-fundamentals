"""
description script:
voy a crear un script que simule el lanzamiento de un dado 
al mismo tiempo que genere un numero del 1 al 6 que al
finalizar los lanzamientos me la suma de todos los valores obtenidos en los lanzamientos

"""


import random

suma_total = 0

# Pedir número de lanzamientos
numero_lanzamientos = int(input("¿Cuántas veces quieres tirar el dado? "))

print("\nIniciando...", numero_lanzamientos, "lanzamientos\n")

# Ciclo de lanzamientos
for i in range(1, numero_lanzamientos + 1):
    dado = random.randint(1, 6)
    suma_total += dado
    print("Lanzamiento", i, ":", dado)

# Resultados finales
print("\nFin de los lanzamientos.")
print("La suma total de todos los valores es:", suma_total)