from datetime import datetime

# Variables generales
empleados_registrados = []
total_empleados = 0
total_genero_M = 0
total_genero_F = 0
total_genero_O = 0
suma_salarios = 0.0
suma_anios_nacimiento = 0

anio_actual = datetime.now().year

# validar texto
def validar_texto(texto):
    if texto == "":
        return False
    for caracter in texto:
        if not (caracter.isalpha() or caracter.isspace()):
            return False
    return True

print("\n === Registro de Empleados ===")
agregar_otro = "s"

while agregar_otro == "s":

    print("\n-- Nuevo Empleado --")
    datos_empleado = {}

    # Nombres
    while True:
        nombre = input("Nombres completos: ")
        if validar_texto(nombre):
            datos_empleado["nombre"] = nombre
            break
        else:
            print("Use solo letras y espacios.")

    # Email
    while True:
        email = input("Email: ")
        if "@" in email and len(email) > 5:
            datos_empleado["email"] = email
            break
        else:
            print("Email no válido.")

    # Móvil
    while True:
        movil = input("Número móvil: ")
        if movil.isdigit() and len(movil) >= 7:
            datos_empleado["movil"] = movil
            break
        else:
            print("Solo números y mínimo 7 dígitos.")

    # Género
    while True:
        genero = input("Género (M/F/O): ").upper()
        if genero in ("M", "F", "O"):
            datos_empleado["genero"] = genero
            break
        else:
            print("Opción no válida.")

    # Salario
    while True:
        salario_str = input("Salario: ")
        try:
            salario = float(salario_str)
            if salario >= 0:
                datos_empleado["salario"] = salario
                break
            else:
                print("Debe ser positivo.")
        except:
            print("Ingrese un número.")

    # Año nacimiento
    while True:
        anio_str = input("Año nacimiento (AAAA): ")
        if anio_str.isdigit() and len(anio_str) == 4:
            anio_nac = int(anio_str)
            if anio_nac >= 1900 and anio_nac <= anio_actual:
                datos_empleado["anio_nacimiento"] = anio_nac
                break
            else:
                print("Año fuera de rango.")
        else:
            print("Ingrese 4 dígitos.")

    # Guardar datos
    empleados_registrados.append(datos_empleado)
    total_empleados += 1
    suma_salarios += datos_empleado["salario"]
    suma_anios_nacimiento += datos_empleado["anio_nacimiento"]

    # Contadores género
    if datos_empleado["genero"] == "M":
        total_genero_M += 1
    elif datos_empleado["genero"] == "F":
        total_genero_F += 1
    else:
        total_genero_O += 1

    # Continuar
    agregar_otro = input("¿Agregar otro? (S/N): ").lower()
    while agregar_otro not in ("s", "n"):
        agregar_otro = input("Solo S o N: ").lower()

# Reporte
print("\n=== REPORTE FINAL ===")
print("Total empleados:", total_empleados)
print("Género M:", total_genero_M)
print("Género F:", total_genero_F)
print("Género O:", total_genero_O)
print("Total salarios: $", format(suma_salarios, ",.2f"))

if total_empleados > 0:
    promedio_anio = suma_anios_nacimiento / total_empleados
    promedio_edad = anio_actual - promedio_anio
    print("Promedio edad:", round(promedio_edad, 1), "años")
else:
    print("No hay empleados registrados.")

print("=======================")
