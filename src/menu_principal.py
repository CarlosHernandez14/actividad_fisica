from src.manejo_archivos.actividadesPickle import ActividadesPickle
from src.clases.Actividad import Actividad
from src.clases.Estudiante import Estudiante


def menu_principal():
    """Muestra el menú principal del juego."""
    
    opciones = """
    1. Registrar Actividad
    2. Cargar Actividades
    3. Guardar Actividades
    4. Ver por estudiante
    5. Estadísticas
    6. Filtrar por fecha
    7. Salir
    """

    print("=" * 35)
    print("Bienvenido al sistema de gestión \n \t de actividades.")
    print("=" * 35)
    print(opciones)
    print("=" * 35)
    opcion = input("Seleccione una opción: ")
    
    while opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
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
        pass
    elif opcion == "5":
        # función para mostrar estadísticas
        pass
    elif opcion == "6":
        # función para filtrar actividades por fecha
        pass
    elif opcion == "7":
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
        
    

def menu_registrar_actividad():
    """Muestra el menú para registrar una actividad."""
    

    print("=" * 35)
    print("Registrar Actividad")
    print("=" * 35)
    
    alumno_id = input("Ingrese el ID del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    actividad = input("Ingrese la actividad: ")
    duracion = input("Ingrese la duración de la actividad (en minutos): ")
    calorias = input("Ingrese las calorías quemadas: ")
    fecha = input("Ingrese la fecha de la actividad (DD/MM/AAAA): ")
    
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
        print("No hay actividades guardadas.")
        
        
    opcion = input("¿Desea volver al menú principal? (s/n): ")
    
    while opcion.lower() not in ["s", "n"]:
        print("Opción inválida. Por favor, seleccione 's' o 'n'.")
        opcion = input("¿Desea volver al menú principal? (s/n): ")
    
    if opcion.lower() == "s":
        menu_principal()
    else:
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
    
    
    