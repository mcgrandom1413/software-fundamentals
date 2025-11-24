from datetime import datetime

# Definición de variables y estructuras de dados
empleados_registrados = []
total_empleados = 0
total_genero_M = 0
total_genero_F = 0
total_genero_O = 0
suma_salarios = 0.0          # Usamos float para la suma de salarios
suma_anios_nacimiento = 0

# Obtenemos el año actual del sistema (es mejor que poner un valor fijo)
anio_actual = datetime.now().year

# =========================================================
# Función para validar si un texto solo contiene letras y espacios
# =========================================================
def validar_texto(texto):
    """Verificamos  si el texto contiene solo letras y espacios."""
    if not texto:
        return False
    # Itera sobre cada carácter para asegurar que solo sean letras o espacios
    for caracter in texto:
        if not (caracter.isalpha() or caracter.isspace()):
            return False
    return True

# Bucle principal para registrar empleados

agregar_otro = 's' # Inicializamos la variable para entrar al bucle

print("=== Sistema de Registro de Empleados ===")

while agregar_otro.lower() == 's':
    print("\n--- Registro de Nuevo Empleado ---")
    datos_empleado = {} # Diccionario temporal para guardar los datos del empleado actual

    # 1. Solicitamos  y validamos  Nombres Completos (debe ser solo texto)
    while True:
        nombre = input("Ingrese Nombres Completos: ")
        if validar_texto(nombre):
            datos_empleado['nombre'] = nombre
            break
        else:
            # Se añade un guion para evitar que la terminal muestre el icono de error (X roja)
            print("- Dato no válido. Use solo letras y espacios. Por ejemplo: Juan Perez.")

    # 2. Solicitar y validar Email (contiene '@' y largo mínimo)
    while True:
        email = input("Ingrese Email: ")
        if '@' in email and len(email) > 5:
            datos_empleado['email'] = email
            break
        else:
            print(" Dato no válido. El email debe contener un '@' y tener un formato coherente.")

    # 3. Solicitar y validar Número Móvil (dígitos y un largo mínimo de 7)
    while True:
        movil = input("Ingrese Número Móvil: ")
        if movil.isdigit() and len(movil) >= 7:
            datos_empleado['movil'] = movil
            break
        else:
            print(" Dato no válido. Ingrese solo números (dígitos) para el móvil.")

    # 4. Solicitar y validar Género (solo M, F, o O)
    while True:
        genero = input("Ingrese Género (M, F, O): ").upper()
        if genero in ('M', 'F', 'O'):
            datos_empleado['genero'] = genero
            break
        else:
            print(" Opción de género no válida. Ingrese solamente M, F o O.")

    # 5. Solicitar y validar Salario (debe ser un número positivo, usando try-except)
    while True:
        salario_str = input("Ingrese Salario: ")
        try:
            salario = float(salario_str)
            if salario >= 0:
                datos_empleado['salario'] = salario
                break
            else:
                print(" El salario debe ser un número positivo.")
        except ValueError:
            print(" Dato no válido. El salario debe ser un número (ej: 1200.50).")

    # 6. Solicitar y validar Año de Nacimiento (AAAA, con rango)
    while True:
        anio_str = input("Ingrese Año de Nacimiento (AAAA): ")
        if anio_str.isdigit() and len(anio_str) == 4:
            anio_nacimiento = int(anio_str)
            # Validación de rango: No antes de 1900 y no posterior al año actual
            if anio_nacimiento >= 1900 and anio_nacimiento <= anio_actual:
                datos_empleado['anio_nacimiento'] = anio_nacimiento
                break
            else:
                print(f" Año no válido. Debe estar entre 1900 y {anio_actual}.")
        else:
            print("- Dato no válido. Ingrese el año con 4 dígitos (AAAA).")

    # =========================================================
    # 7. Guardar datos del empleado y actualizar contadores
    # =========================================================
    empleados_registrados.append(datos_empleado)
    total_empleados += 1
    suma_salarios += datos_empleado['salario']
    suma_anios_nacimiento += datos_empleado['anio_nacimiento']

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
            print(" Respuesta no válida. Ingrese solo S o N.")

# =========================================================
# REPORTE FINAL
# =========================================================

print("\n\n=======================================")
print(" REPORTE FINAL DE EMPLEADOS")
print("=======================================")

# 1. Total de Empleados
print(f"- Total de empleados registrados: {total_empleados}")

# 2. Total por Género
print(f"- Total Género M: {total_genero_M}")
print(f"- Total Género F: {total_genero_F}")
print(f"- Total Género O: {total_genero_O}")

# 3. Total Salarios
# Formato con separador de miles y dos decimales
print(f"- Total de salarios a pagar: ${suma_salarios:,.2f}")

# 4. Promedio de Edades
if total_empleados > 0:
    # Cálculo del promedio de edad
    promedio_anio_nac = suma_anios_nacimiento / total_empleados
    promedio_edad = anio_actual - promedio_anio_nac
    
    # Muestra el promedio de edad con un decimal
    print(f"- Promedio de edades: {promedio_edad:.1f} años")
else:
    print("- No se registraron empleados, por lo tanto no hay promedio de edades.")

print("=======================================")




