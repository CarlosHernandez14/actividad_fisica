
class Actividad:
    """Clase que representa una actividad."""

    def __init__(self, alumno_id, nombre, actividad, duracion_min, calorias, fecha):
        self.alumno_id = alumno_id
        self.nombre = nombre
        self.actividad = actividad
        self.duracion_min = duracion_min
        self.calorias = calorias
        self.fecha = fecha
        
    def mostrar_informacion(self):
        """Muestra la información de la actividad."""
        print(f"ID Alumno: {self.alumno_id}")
        print(f"Nombre: {self.nombre}")
        print(f"Actividad: {self.actividad}")
        print(f"Duración (min): {self.duracion_min}")
        print(f"Calorías quemadas: {self.calorias}")
        print(f"Fecha: {self.fecha}")


    def __str__(self):
        return f"Actividad: {self.nombre}, Fecha: {self.fecha}, Tipo: {self.tipo}, Descripción: {self.descripcion}"

    def __repr__(self):
        return f"Actividad({self.nombre}, {self.fecha}, {self.tipo}, {self.descripcion})"