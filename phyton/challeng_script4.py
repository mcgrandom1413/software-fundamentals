import random
random.seed()   #Prepare random number generator

print("press enter to roll")
iniciando = input()
print("ingresa cuantos numeros de lanzamientos ")
numLanz = int(input())
print("iniciando" + str(numLanz) + " veces ")
for i in range(1, numLanz + 1, 1):
    dado1 = int(random.random() * 6) + 1
    dado2 = int(random.random() * 6) + 1
    print("lanzamiento" + str(i) + ": " + str(dado1) + " y " + str(dado2))
    if dado1 == 6 and dado2 == 6:
        i = numLanz
        print(" ¡ oh ! par de seis obtenido" + " game over ")
print("gracias por jugar")