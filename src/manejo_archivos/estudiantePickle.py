import pickle

class EstudiantePickle:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def guardar_estudiantes(self, estudiantes):
        with open(self.nombre_archivo, 'wb') as archivo:
            pickle.dump(estudiantes, archivo)

    def cargar_estudiantes(self):
        try:
            with open(self.nombre_archivo, 'rb') as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            return []