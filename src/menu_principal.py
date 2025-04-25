from src.manejo_archivos.actividadesPickle import ActividadesPickle
from src.manejo_archivos.estudiantePickle import EstudiantePickle
from src.clases.Actividad import Actividad
from src.clases.Estudiante import Estudiante
from src.menus.menu_estadisticas import menu_estadisticas


def menu_principal():
    """Muestra el menú principal de la app."""
    
    opciones = """
    1. Registrar Actividad
    2. Cargar Actividades
    3. Guardar Actividades
    4. Ver por estudiante
    5. Estadísticas
    6. Filtrar por fecha
    7. Estudiantes 
    8. Salir
    """

    print("=" * 35)
    print("Bienvenido al sistema de gestión \n \t de actividades.")
    print("=" * 35)
    print(opciones)
    print("=" * 35)
    opcion = input("Seleccione una opción: ")
    
    while opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        opcion = input("Seleccione una opción: ")
        
    if opcion == "1":
        menu_registrar_actividad()
    elif opcion == "2":
        # función para cargar actividades
        menu_cargar_actividades()
    elif opcion == "3":
        # función para guardar actividades
        pass
    elif opcion == "4":
        # función para ver actividades por estudiante
        ver_por_estudiante()
    elif opcion == "5":
        # función para mostrar estadísticas
        menu_estadisticas()
    elif opcion == "6":
        # función para filtrar actividades por fecha
        filtrar_por_fecha()
    elif opcion == "7":
        # función para ver menu de estudiantes
        menu_estudiantes()
    elif opcion == "8":
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
        
    

def menu_registrar_actividad():
    """Muestra el menú para registrar una actividad."""
    

    print("=" * 35)
    print("Registrar Actividad")
    print("=" * 35)
    
    alumno_id = input("Ingrese el ID del estudiante: ")
    
    # Verificar si el estudiante existe
    estudiantePickle = EstudiantePickle("estudiantes.pkl")
    existeEstudiante = estudiantePickle.verficar_estudiante(id_estudiante=alumno_id)
    
    if not existeEstudiante:
        print("El estudiante no existe. Por favor, registre al estudiante primero.")
        menu_estudiantes()
        return
    
    nombre = input("Ingrese el nombre de la actividad: ")
    actividad = input("Ingrese el tipo de actividad: ")
    duracion = input("Ingrese la duración de la actividad (en minutos): ")
    calorias = input("Ingrese las calorías quemadas: ")
    fecha = input("Ingrese la fecha de la actividad (YYYY-MM-DD HH:MM:SS): ")
    
    # Convertir la fecha a un formato adecuado
    try:
        from datetime import datetime
        fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
        print(f"Fecha convertida: {fecha}")
    except ValueError:
        print("❌ Formato de fecha inválido. Por favor, use el formato YYYY-MM-DD HH:MM:SS.")
        input("Presione Enter para continuar...")
        menu_principal()
        return
    
    actividad = {
        "alumno_id": alumno_id,
        "nombre": nombre,
        "actividad": actividad,
        "duracion": duracion,
        "calorias": calorias,
        "fecha": fecha
    }
    
    actividad = Actividad(actividad)
    
    # Guardar la actividad en un archivo usando pickle
    actividades = ActividadesPickle("actividades.pkl")
    actividades_guardadas = actividades.cargar_actividades()
    
    if actividades_guardadas:
        actividades_guardadas.append(actividad)
    else:
        actividades_guardadas = [actividad]
    
    actividades.guardar_actividades(actividades_guardadas)
    
    input("Presione Enter para continuar...")
    # Regresamos al menu principal 
    menu_principal()
    
    

def menu_cargar_actividades():
    """Carga las actividades desde el archivo."""
    
    actividades = ActividadesPickle("actividades.pkl")
    actividades_guardadas = actividades.cargar_actividades()
    
    if actividades_guardadas:
        print("Actividades cargadas:")
        for actividad in actividades_guardadas:
            print(actividad)
    else:
        print("❌ No hay actividades guardadas.")
        
        
    opcion = input("¿Desea volver al menú principal? (s/n): ")
    
    while opcion.lower() not in ["s", "n"]:
        print("Opción inválida. Por favor, seleccione 's' o 'n'.")
        opcion = input("¿Desea volver al menú principal? (s/n): ")
    
    if opcion.lower() == "s":
        menu_principal()
    else:
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
    
    
def menu_estudiantes():
    """Muestra el menú para gestionar estudiantes."""
    
    print("=" * 35)
    print("Gestión de Estudiantes")
    print("=" * 35)
    
    opciones = """
    1. Agregar Estudiante
    2. Ver Estudiantes
    3. Eliminar Estudiante
    4. Volver al menú principal
    """
    
    print(opciones)
    
    
    opcion = input("Seleccione una opción: ")
    
    while opcion not in ["1", "2", "3", "4"]:
        print("❌ Opción inválida. Por favor, seleccione una opción válida.")
        opcion = input("Seleccione una opción: ")
        
    estudiantePickle = EstudiantePickle("estudiantes.pkl")
    
    if opcion == "1":
        # función para agregar estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = input("Ingrese la edad del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")
        
        # Crear un objeto Estudiante
        estudiante = Estudiante(nombre, edad, carrera)
        
        estudiantePickle.agregar_estudiante(estudiante)
        print("✅ Estudiante agregado exitosamente.")
        menu_estudiantes()
    elif opcion == "2":
        # función para ver estudiantes
        estudiantes = estudiantePickle.cargar_estudiantes()
        if estudiantes:
            print("Estudiantes registrados:")
            for estudiante in estudiantes:
                print(estudiante)
        else:
            print("❌ No hay estudiantes registrados.")
            
        input("Presione Enter para continuar...")
        # Regresar al menú de estudiantes
        menu_estudiantes()
    elif opcion == "3":
        # función para eliminar estudiante
        id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")
        estudiantePickle.eliminar_estudiante(id_estudiante=id_estudiante)
        menu_estudiantes()
    elif opcion == "4":
        menu_principal()
        
def ver_por_estudiante():
    """Ver actividades por estudiante."""
    
    # Cargar actividades desde el archivo
    actividades = ActividadesPickle("actividades.pkl")
    actividades_guardadas = actividades.cargar_actividades()
    estudiantePickle = EstudiantePickle("estudiantes.pkl")
    
    estudiantes = estudiantePickle.cargar_estudiantes()
    
    if actividades_guardadas:
        print("Actividades registradas por estudiante:")
        for estudiante in estudiantes:
            print(f"ESTUDIANTE: {estudiante.nombre} (ID: {estudiante.id})")
            actividades_estudiante = [actividad for actividad in actividades_guardadas if actividad.alumno_id == estudiante.id]
            print("-" * 35)
            print("Actividades del estudiante:")
            if actividades_estudiante:
                for actividad in actividades_estudiante:
                    print(f"{actividad}")
            else:
                print("-" * 35)
                print("\n❌ No hay actividades registradas para este estudiante.\n")
                print("-" * 35)
        print("=" * 35)
    else:
        print("❌ No hay actividades registradas.")
        
    input("Presione Enter para continuar...")
    menu_principal()
    
def filtrar_por_fecha():
    """Filtrar actividades por fecha."""
    
    # Cargar actividades desde el archivo
    actividades = ActividadesPickle("actividades.pkl")
    actividades_guardadas = actividades.cargar_actividades()
    
    if actividades_guardadas:
        fecha = input("Ingrese la fecha (DD/MM/AAAA) para filtrar: ")
        actividades_filtradas = [actividad for actividad in actividades_guardadas if actividad.fecha == fecha]
        
        if actividades_filtradas:
            print(f"Actividades registradas en la fecha {fecha}:")
            for actividad in actividades_filtradas:
                print(actividad)
        else:
            print(f"❌ No hay actividades registradas en la fecha {fecha}.")
    else:
        print("❌ No hay actividades registradas.")
        
    input("Presione Enter para continuar...")
    menu_principal()