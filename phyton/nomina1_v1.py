# =========================================================
# Definición de variables para almacenar los datos
# =========================================================
empleados_registrados = []
total_empleados = 0
total_genero_M = 0
total_genero_F = 0
total_genero_O = 0
suma_salarios = 0
suma_anios_nacimiento = 0
anio_actual = 2025  # Definimos el año actual para calcular la edad

# =========================================================
# Función para validar si un texto solo contiene letras y espacios (para nombres)
# Nota: Se añade simple validación de longitud para simular un nombre completo.
# =========================================================
def validar_texto(texto, min_letras=8):
    """Verifica si el texto contiene solo letras y espacios y si tiene una longitud mínima."""
    # 1. Verificar si tiene la longitud mínima requerida
    if len(texto.strip()) < min_letras:
        return False
    
    # 2. Verificar que solo contenga letras y espacios
    for caracter in texto:
        if not (caracter.isalpha() or caracter.isspace()):
            return False
            
    # Si pasa ambas verificaciones
    return True

# =========================================================
# Bucle principal para registrar empleados
# =========================================================
agregar_otro = 's' # Inicializamos la variable para entrar al bucle

print("=== Sistema de Registro de Empleados ===")

while agregar_otro.lower() == 's':
    print("\n--- Registro de Nuevo Empleado ---")
    datos_empleado = {}

    # 1. Solicitar y validar Nombres Completos (debe ser solo texto y con mínimo de letras)
    while True:
        nombre = input("Ingrese Nombres Completos (Mínimo 8 letras): ")
        # Usamos la función modificada para la validación
        if validar_texto(nombre, min_letras=6):
            datos_empleado['nombre'] = nombre
            break
        else:
            print("Error: Use solo letras y espacios, y debe tener al menos 6 caracteres. Por ejemplo: Juan Perez.")

    # 2. Solicitar y validar Email (solo una verificación básica de que contiene '@')
    while True:
        email = input("Ingrese Email: ")
        if '@' in email and len(email) > 8: # Validación sencilla
            datos_empleado['email'] = email
            break
        else:
            print("Error: El email debe contener un '@' y tener un formato coherente.")

    # 3. Solicitar y validar Número Móvil (debe ser un número entero)
    while True:
        movil = input("Ingrese Número Móvil: ")
        if movil.isdigit() and len(movil) >= 10: # Verifica que sean solo dígitos y un largo mínimo
            datos_empleado['movil'] = movil
            break
        else:
            print("Error: Ingrese solo números (dígitos) para el móvil.")

    # 4. Solicitar y validar Género (solo M, F, o O)
    while True:
        genero = input("Ingrese Género (M, F, O): ").upper() # Convertimos a mayúscula para simplificar
        if genero in ('M', 'F', 'O'):
            datos_empleado['genero'] = genero
            break
        else:
            print("Error: Opción de género no válida. Ingrese solamente M, F o O.")

    # 5. Solicitar y validar Salario (debe ser un número, puede ser con decimales)
    while True:
        salario_str = input("Ingrese Salario: ")
        try:
            # Intenta convertir a número con decimales
            salario = float(salario_str)
            if salario >= 0:
                datos_empleado['salario'] = salario
                break
            else:
                print("Error: El salario debe ser un número positivo.")
        except ValueError:
            print("Error: El salario debe ser un número (ej: 1200.50).")

    # 6. Solicitar y validar Año de Nacimiento (AAAA) - Incluye validación de edad mínima
    while True:
        anio_str = input("Ingrese Año de Nacimiento (AAAA): ")
        if anio_str.isdigit() and len(anio_str) == 4:
            anio_nacimiento = int(anio_str)
            
            # Validación de año coherente (ej: 1900 hasta el año actual)
            if anio_nacimiento >= 1900 and anio_nacimiento <= anio_actual:
                
                # *** Validación de edad mínima (Menor a 18 años) ***
                edad = anio_actual - anio_nacimiento
                if edad >= 18:
                    datos_empleado['anio_nacimiento'] = anio_nacimiento
                    break
                else:
                    print(f"Error: La edad calculada es de {edad} años. El empleado debe ser mayor o igual a 18 años para el registro.")
            else:
                print(f"Error: Año no válido. Debe estar entre 1900 y {anio_actual}.")
        else:
            print("Error: Ingrese el año con 4 dígitos (AAAA).")

    # Guardar datos del empleado y actualizar contadores
    empleados_registrados.append(datos_empleado)
    total_empleados += 1
    suma_salarios += datos_empleado['salario']
    suma_anios_nacimiento += datos_empleado['anio_nacimiento']

    # Contar por género (sencillo con if/elif/else)
    if datos_empleado['genero'] == 'M':
        total_genero_M += 1
    elif datos_empleado['genero'] == 'F':
        total_genero_F += 1
    elif datos_empleado['genero'] == 'O':
        total_genero_O += 1

    # Preguntar si desea agregar otro empleado
    while True:
        print("\n-------------------------------------")
        agregar_otro = input("¿Desea agregar otro empleado? (S/N): ").lower()
        if agregar_otro in ('s', 'n'):
            break
        else:
            print("Respuesta no válida. Ingrese solo S o N.")

# =========================================================
# Generar el Reporte Final
# =========================================================

print("\n\n=======================================")
print("REPORTE FINAL DE EMPLEADOS")
print("=======================================")

# 1. Total de Empleados
print(f"Total de empleados registrados: {total_empleados}")

# 2. Total por Género
print(f"  - Total Género M: {total_genero_M}")
print(f"  - Total Género F: {total_genero_F}")
print(f"  - Total Género O: {total_genero_O}")

# 3. Total Salarios
# Usamos '{:.2f}'.format() para que el número tenga dos decimales (como moneda)
print(f"Total de salarios a pagar: ${'{:.2f}'.format(suma_salarios)}")

# 4. Promedio de Edades
if total_empleados > 0:
    # Cálculo sencillo del promedio de edad
    promedio_anio_nac = suma_anios_nacimiento / total_empleados
    promedio_edad = anio_actual - promedio_anio_nac
    # Usamos round() para mostrar un promedio de edad sin tantos decimales
    print(f"Promedio de edades: {round(promedio_edad, 1)} años")
else:
    print("No se registraron empleados, por lo tanto no hay promedio de edades.")

print("=======================================")