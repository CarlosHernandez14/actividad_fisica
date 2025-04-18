
class Actividad:
    """Clase que representa una actividad."""

    def __init__(self, actividad_dict):
        self.alumno_id = actividad_dict["alumno_id"]
        self.nombre = actividad_dict["nombre"]
        self.actividad = actividad_dict["actividad"]
        self.duracion_min = actividad_dict["duracion"]
        self.calorias = actividad_dict["calorias"]
        self.fecha = actividad_dict["fecha"]
        
    def mostrar_informacion(self):
        """Muestra la información de la actividad."""
        print(f"ID Alumno: {self.alumno_id}")
        print(f"Nombre: {self.nombre}")
        print(f"Actividad: {self.actividad}")
        print(f"Duración (min): {self.duracion_min}")
        print(f"Calorías quemadas: {self.calorias}")
        print(f"Fecha: {self.fecha}")


    def __str__(self):
        return (
            f"-----------------------------------\n"
            f" Actividad: {self.actividad}\n"
            f" Duración: {self.duracion_min} min\n"
            f" Calorías: {self.calorias}\n"
            f" Fecha: {self.fecha}\n"
            f"------------------------------------"
        )

    def __repr__(self):
        return f"Actividad({self.nombre}, {self.fecha}, {self.tipo}, {self.descripcion})"