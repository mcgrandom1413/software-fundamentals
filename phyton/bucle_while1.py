import os

# --- Inicialización de Variables ---
status = True
total_suma = 0
total_numeros = 0
total_pares = 0
total_impares = 0
total_positivos = 0
total_negativos = 0
total_pares_positivos = 0
total_pares_negativos = 0
total_impares_positivos = 0
total_impares_negativos = 0

os.system("clear")

# --- Bucle Principal de Entrada de Datos ---
print(">>> Análisis de Números (Ingrese 0 para terminar) <<<")

while status:
    try:
        num = int(input("Ingrese un número entero: "))
    except ValueError:
        print("¡Error! Ingrese un número entero válido.")
        continue
   

    if num == 0:
        status = False
        break

    # Contadores y Sumador General
    total_numeros += 1
    total_suma += num
    
    # Clasificación Par/Impar
    es_par = (num % 2 == 0)

    if es_par:
        total_pares += 1
    else:
        total_impares += 1
        
    # Clasificación Positivo/Negativo y Combinaciones
    if num > 0:
        total_positivos += 1
        if es_par:
            total_pares_positivos += 1
        else:
            total_impares_positivos += 1
            
    elif num < 0:
        total_negativos += 1
        if es_par:
            total_pares_negativos += 1
        else:
            total_impares_negativos += 1       




# --- Impresión de Resultados ---

print("------------------------------------" + "\n" "    :D   :D    RESULTADOS :D   :D" "\n"+"-------------------------------------\n")
if total_numeros == 0:
    print("No se ingresó ningún número para analizar.")
else:
    print(f" Total de números ingresados: {total_numeros}")
    print(f" Suma total: {total_suma}\n")
    print("--- Clasificación General ---")
    print(f"  Pares: {total_pares} | Impares: {total_impares}")
    print(f"  Positivos: {total_positivos} | Negativos: {total_negativos}\n")
    print("--- Clasificación Detallada ---")
    print(f"  Pares Positivos: {total_pares_positivos}")
    print(f"  Pares Negativos: {total_pares_negativos}")
    print(f"  Impares Positivos: {total_impares_positivos}")
    print(f"  Impares Negativos: {total_impares_negativos}")





