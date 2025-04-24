from src.manejo_archivos.estudiantePickle import EstudiantePickle
from src.manejo_archivos.actividadesPickle import ActividadesPickle


def getCaloriasPorEstudiante():
    """
    Esta función calcula las calorías por estudiante y por grupo.
    :return: Calorías por estudiante
    """
    estudiantesPickle = EstudiantePickle("estudiantes.pkl")
    actividadesPickle = ActividadesPickle("actividades.pkl")
    
    estudiantes = estudiantesPickle.cargar_estudiantes()
    actividades = actividadesPickle.cargar_actividades()
    """
    "Alice": 450,
    "Bob": 320,
    "Carlos": 600,
    """
    caloriasPorEstudiante = {}
    
    for actividad in actividades:
        if actividad.alumno_id not in caloriasPorEstudiante:
            caloriasPorEstudiante[actividad.alumno_id] = 0
        caloriasPorEstudiante[actividad.alumno_id] += int(actividad.calorias)
        
    for estudiante in estudiantes:
        if estudiante.id in caloriasPorEstudiante:
            # Reemplaza el ID del estudiante por su nombre
            caloriasPorEstudiante[estudiante.nombre] = caloriasPorEstudiante[estudiante.id]
            del caloriasPorEstudiante[estudiante.id]
        else:
            caloriasPorEstudiante[estudiante.nombre] = 0

    return caloriasPorEstudiante
    
def promedioCaloriasPorActividad():
    """
    Esta función calcula el promedio de calorías por actividad.
    :param actividades: Lista de actividades
    :return: Promedio de calorías por actividad
    """
    actividadesPickle = ActividadesPickle("actividades.pkl")
    actividades = actividadesPickle.cargar_actividades()
    
    # Calorías por actividad (Dict)
    # "Correr": [450, 320, 600],
    caloriasPorActividad = {}
    
    for actividad in actividades:
        if actividad.actividad not in caloriasPorActividad:
            caloriasPorActividad[actividad.actividad] = []
        caloriasPorActividad[actividad.actividad].append(int(actividad.calorias))
        
    # Promedio de calorías por actividad (Dict)
    # "Correr": 450,
    promedioPorActividad = {}

    # Calcular el promedio de calorías por actividad
    # Nombre de actividad: [caloriasLista]    
    for actividad, calorias in caloriasPorActividad.items():
        promedioPorActividad[actividad] = sum(calorias) / len(calorias)
        
    return promedioPorActividad

def diasConMasActividades():
    """
    Esta función calcula los días con más actividades.
    :return: Diccionario con la cantidad de actividades por día.
    """
    actividadesPickle = ActividadesPickle("actividades.pkl")
    actividadesCargadas = actividadesPickle.cargar_actividades()
    
    # Diccionario para agrupar actividades por fecha
    diasConMasActividades = {}
    
    for actividad in actividadesCargadas:
        # Obtener solo la fecha (sin la hora)
        fechaSinHora = actividad.fecha.date().strftime("%Y-%m-%d")
        if fechaSinHora not in diasConMasActividades:
            diasConMasActividades[fechaSinHora] = []
        diasConMasActividades[fechaSinHora].append(actividad)
        
    # Diccionario con la cantidad de actividades por día
    diasConMasActividadesCount = {}
    
    for fecha, listaActividades in diasConMasActividades.items():
        cantidad = len(listaActividades)
        diasConMasActividadesCount[fecha] = cantidad
    print("-" * 35)

    return diasConMasActividadesCount

def actividadesOrdenadasPorFecha():
    """
    Esta función ordena las actividades por fecha.
    :return: Lista de actividades ordenadas por fecha.
    """
    actividadesPickle = ActividadesPickle("actividades.pkl")
    actividadesCargadas = actividadesPickle.cargar_actividades()
    
    # Ordenar las actividades por fecha
    actividadesOrdenadas = sorted(actividadesCargadas, key=lambda x: x.fecha)
    
    return actividadesOrdenadas

def buscarAlumnoPorID(alumno_id):
    """
    Esta función busca un alumno por su ID.
    :param alumno_id: ID del alumno a buscar
    :return: Alumno encontrado o None si no se encuentra
    """
    estudiantesPickle = EstudiantePickle("estudiantes.pkl")
    estudiantes = estudiantesPickle.cargar_estudiantes()
    
    for estudiante in estudiantes:
        if estudiante.id == alumno_id:
            return estudiante
    
    return None
