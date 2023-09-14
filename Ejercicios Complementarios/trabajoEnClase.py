import sys

# VERIFICACIÓN DE DIAS SEMANALES
def verificar_dia_valida(dia, dias_validos):
    for elemento in dias_validos:
        if dia == elemento:
            return True  # El dato ingresado es igual a algún elemento del arreglo
    return False  # El dato ingresado es diferente a todos los elementos del arreglo

# VERIFICACIÓN DE DÍAS DD:
def verificar_dd_valido(dd):
    if dd <= 31 and dd >= 1:
        return True
    else: 
        return False

# VERIFICACIÓN DE MESES:
def verificar_mm_valido(mm):
    if mm <= 12 and mm >= 1:
        return True
    else: 
        return False

# EXAMENES
def verificar_si_hubo_examen_opcion1(dia):
    if dia in ["lunes", "martes", "miercoles"]:
        respuesta = input("Hubo Examen ese día? s/n: ").lower()
        return respuesta
    elif dia == "jueves":
        return False
    elif dia == "viernes":
        return None
    else:
        print("No se dictan clases los días Sábados y Domingos")

fecha_actual = input("Ingrese la fecha actual en formato dia/DD/MM: (sin tildes)")
fecha_actual = fecha_actual.lower()
dia, dd, mm = map(str, fecha_actual.split('/'))
dd = int(dd)
mm = int(mm)

dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

if verificar_dia_valida(dia, dias_validos) == False:
    print("Error, ingrese un día correcto")
    sys.exit()

if verificar_dd_valido(dd) == False:
    print("Error, ingrese un dd correcto")
    sys.exit()

if verificar_mm_valido(mm) == False:
    print("Error, ingrese un mm correcto")
    sys.exit()

respuesta_examen = verificar_si_hubo_examen_opcion1(dia)

if respuesta_examen == "n":
    print("Terminando la ejecución.")
    sys.exit()

if respuesta_examen == "s":
    print("Hubo examen, siga las instrucciones:")
    alumnos_aprobados = int(input("Ingrese la cantidad de alumnos que aprobaron: "))
    alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos que desaprobaron: "))
    promedio_aprobados = (alumnos_aprobados / (alumnos_aprobados + alumnos_desaprobados)) * 100
    print("El porcentaje de aprobados es de:", promedio_aprobados, "%")
elif respuesta_examen == False:
    porcentaje_asistencia = int(input("Ingrese el porcentaje de alumnos que asistieron a clase (SIN %): "))
    if porcentaje_asistencia > 50:
        print("Asistió la mayoría")
    elif porcentaje_asistencia == 50:
        print("Asistió la mitad de la clase")
    else:
        print("No asistió la mayoría")
elif respuesta_examen is None:
    if dd == 1 and mm in [1, 7]:
        print("Comienzo de nuevo ciclo")
        cantidad_alumnos = int(input("Por favor, ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = float(input("Por favor, ingrese el arancel por alumno: "))
        total_arancel = cantidad_alumnos * arancel
        print("El ingreso total es de", total_arancel, "$")
    else:
        print("Día no válido para iniciar un nuevo ciclo")