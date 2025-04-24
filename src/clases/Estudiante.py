
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        
        # Generar un ID único para cada estudiante
        self.id = self.generar_id_estudiante()
        
    def generar_id_estudiante(self):
        # Genera un ID único basado en el nombre y la edad
        return f"{self.nombre[:3].upper()}{self.edad}{hash(self.nombre) % 1000}"

    def mostrar_informacion(self):
        """Muestra la información del estudiante."""
        print(f"ID Estudiante: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        
    def __str__(self):
        return (
            f"-----------------------------------\n"
            f" ID: {self.id}\n"
            f" Nombre: {self.nombre}\n"
            f" Edad: {self.edad}\n"
            f" Carrera: {self.carrera}\n"
            f"------------------------------------"
        )