import random
random.seed()   #Prepare random number generator

pares = 0
impares = 0
print("press enter to roll dice ")
iniciar = input()
print(" cuantas veces quieres tirar los dados ")
numLanz = int(input())
print(" Iniciando " + str(numLanz) + " veces ")
for i in range(1, numLanz + 1, 1):
    dado1 = int(random.random() * 6) + 1
    dado2 = int(random.random() * 6) + 1
    print(" lanzamiento " + str(i) + " : " + str(dado1) + " y " + str(dado2))
    if dado1 % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if dado2 % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print("fin de ls lanzamientos")
print("total de numeros pares  : " + str(pares))
print("  total de numero impares : " + str(impares))
print("gracias por jugar")