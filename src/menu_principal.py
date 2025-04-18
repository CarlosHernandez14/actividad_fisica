

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
        # Aquí puedes llamar a la función para cargar actividades
        pass
    elif opcion == "3":
        # Aquí puedes llamar a la función para guardar actividades
        pass
    elif opcion == "4":
        # Aquí puedes llamar a la función para ver actividades por estudiante
        pass
    elif opcion == "5":
        # Aquí puedes llamar a la función para mostrar estadísticas
        pass
    elif opcion == "6":
        # Aquí puedes llamar a la función para filtrar actividades por fecha
        pass
    elif opcion == "7":
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
        
    

def menu_registrar_actividad():
    """Muestra el menú para registrar una actividad."""
    
    opciones = """
    1. Registrar Actividad
    2. Volver al menú principal
    """

    print("=" * 35)
    print("Registrar Actividad")
    print("=" * 35)
    print(opciones)
    print("=" * 35)
    opcion = input("Seleccione una opción: ")
    
    while opcion not in ["1", "2"]:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        # Aquí puedes llamar a la función para registrar actividad
        pass
    elif opcion == "2":
        # Aquí puedes llamar a la función para volver al menú principal
        menu_principal()