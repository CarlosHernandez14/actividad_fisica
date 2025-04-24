import pickle

class EstudiantePickle:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        
    def agregar_estudiante(self, estudiante):
        estudiantes = self.cargar_estudiantes()
        estudiantes.append(estudiante)
        self.guardar_estudiantes(estudiantes)

    def guardar_estudiantes(self, estudiantes):
        try:
            with open(self.nombre_archivo, 'wb') as archivo:
                pickle.dump(estudiantes, archivo)
                # print("Estudiantes guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar estudiantes: {e}")

    def cargar_estudiantes(self):
        try:
            with open(self.nombre_archivo, 'rb') as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            return []
        
    def eliminar_estudiante(self, id_estudiante):
        estudiantes = self.cargar_estudiantes()
        estudiantes = [estudiante for estudiante in estudiantes if estudiante.id != id_estudiante]
        self.guardar_estudiantes(estudiantes)
        print(f"Estudiante con ID {id_estudiante} eliminado correctamente.")
        
    def verficar_estudiante(self, id_estudiante):
        estudiantes = self.cargar_estudiantes()
        for estudiante in estudiantes:
            if estudiante.id == id_estudiante:
                return True
        return False