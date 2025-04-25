from src.manejo_archivos.actividadesPickle import ActividadesPickle
from src.manejo_archivos.estudiantePickle import EstudiantePickle
from src.clases.Actividad import Actividad
from src.clases.Estudiante import Estudiante
from src.utils.util_functions import getCaloriasPorEstudiante, promedioCaloriasPorActividad, diasConMasActividades
from src.utils.util_functions import actividadesOrdenadasPorFecha, buscarAlumnoPorID
from src.manejo_archivos.reportesPdf import generar_reporte_pdf

def menu_estadisticas():
    """Muestra el menú de estadísticas."""
    from src.menu_principal import menu_principal
    
    opciones = """
    1. Total de calorías por estudiante
    2. Promedio de calorías por actividad
    3. Días con más actividades
    4. Actividades ordenadas por fecha
    5. Buscar alumno por ID
    6. Generar reporte PDF
    7. Regresar al menú principal
    """
    
    print("=" * 35)
    print("Bienvenido al menú de estadísticas.")
    print("=" * 35)
    print(opciones)
    print("=" * 35)
    
    opcion = input("Seleccione una opción: ")
    
    # Validar la opción ingresada
    # Asegurarse de que la opción sea un número entre 1 y 6
    while opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
        # si la opción no es válida, mostrar un mensaje de error y volver a pedir la opción
        print("Opción inválida. Por favor, seleccione una opción válida.")
        opcion = input("Seleccione una opción: ")
        
    # Ejecutar la opción seleccionada
    if opcion == "1":
        caloriasPorEstudiante = getCaloriasPorEstudiante()
        print("Calorías por estudiante:")
        
        print("-" * 35)
        # Mostrar las calorías por estudiante
        for estudiante, calorias in caloriasPorEstudiante.items():
            print(f"{estudiante}: {calorias} calorías")
        print("-" * 35)
        
        input("Presione Enter para continuar...")
        menu_principal()
    elif opcion == "2":
        # función para calcular promedio de calorías por actividad
        promedioCalPorAct = promedioCaloriasPorActividad()
        print("Promedio de calorías por actividad:")
        print("-" * 35)
        # Mostrar el promedio de calorías por actividad
        for actividad, promedio in promedioCalPorAct.items():
            print(f"{actividad}: {promedio} calorías")
        print("-" * 35)
        
        input("Presione Enter para continuar...")
        menu_estadisticas()
    elif opcion == "3":
        # función para mostrar días con más actividades
        diasConMasAct = diasConMasActividades()
        print("Días con más actividades:")
        
        print("-" * 35)
        # Mostrar los días con más actividades
        for fecha, actividades in diasConMasAct.items():
            print(f"{fecha}: {actividades} actividades")
        print("-" * 35)
        
        input("Presione Enter para continuar...")
        menu_estadisticas()
    elif opcion == "4":
        # función para mostrar actividades ordenadas por fecha
        actividadesPorFecha = actividadesOrdenadasPorFecha()
        print("Actividades ordenadas por fecha:")
        
        print("-" * 35)
        for actividad in actividadesPorFecha:
            print(actividad)
        print("-" * 35)
        
        input("Presione Enter para continuar...")
        menu_estadisticas()
    elif opcion == "5":
        # función para buscar alumno por ID
        id_alumno = input("Ingrese el ID del alumno: ")
        estudiante = buscarAlumnoPorID(id_alumno)
        if estudiante:
            print("Información del alumno:")
            print(estudiante)
        else:
            print("-" * 35)
            print("\n❌ Alumno no encontrado.\n")
            print("-" * 35)
        input("Presione Enter para continuar...")
        menu_estadisticas()
    elif opcion == "6":
        # función para generar reporte PDF
        nombre_archivo = input("Ingrese el nombre del archivo PDF (sin extensión): ") + ".pdf"
        generar_reporte_pdf(nombre_archivo)
        
        input("Presione Enter para continuar...")
        menu_estadisticas()
    elif opcion == "7":
        menu_principal()
