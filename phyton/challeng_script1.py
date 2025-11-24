"""
description script:
voy a crear un script que simule el lanzamiento de un dado 
al mismo tiempo que genere un numero del 1 al 6 y me diga si es par o impar

"""
import random

# iniciando lanzamiento del dado
input("Presiona Enter para lanzar el dado...")

print("Dado lanzado correctamente")

# Generando número aleatorio entre 1 y 6
dado = random.randint(1, 6)

print("Dice:", dado)

# es par o impar
if dado % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")

print("Gracias por jugar.")