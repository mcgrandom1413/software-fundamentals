import random
random.seed()   #Prepare random number generator


# declare variables
dado1 = 0
dado2 = 0
print(" press  enter to roll dices ")
realsetime = input()
dado1 = int(random.random() * 6) + 1
dado2 = int(random.random() * 6) + 1
print(" el resultados del dado 1 es :" + str(dado1))
print(" el resultado del dado 2 es: " + str(dado2))
if dado1 % 2 == 0:
    print(" el resultado de dado 1: Es par  ")
else:
    print(" su resultado de dado 1: Es impar ")
if dado2 % 2 == 0:
    print(" el resultado de dado 2: Es par ")
else:
    print(" el resultado de dado 2 : Es impar ")
if dado1 == dado2:
    result = dado1 == dado2
    print("¡ you win !")
else:
    print("game over ")
