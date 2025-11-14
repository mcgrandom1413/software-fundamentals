"""
srcript decription: 
voy a elaborar 

"""



import random

# esperano que el usuario le de enter para iniciar
input("Presiona Enter para iniciar...")

# Contadores de cada numero que tiene cada cara del dado
c1 = c2 = c3 = c4 = c5 = c6 = 0

# cantidad de lanzamientos
n = int(input("¿Cuántas veces deseas lanzar el dado? "))

# Lanzar n veces
for i in range(1, n + 1):
    dado = random.randint(1, 6)
    
    if dado == 1:
        c1 += 1
    elif dado == 2:
        c2 += 1
    elif dado == 3:
        c3 += 1
    elif dado == 4:
        c4 += 1
    elif dado == 5:
        c5 += 1
    else:
        c6 += 1

# Mostrar resultados
print("\nResultados:")
print("1 salió", c1, "veces")
print("2 salió", c2, "veces")
print("3 salió", c3, "veces")
print("4 salió", c4, "veces")
print("5 salió", c5, "veces")
print("6 salió", c6, "veces")