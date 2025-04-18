import pickle

class ActividadesPickle:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def guardar_actividades(self, actividades):
        try:
            with open(self.nombre_archivo, 'wb') as archivo:
                pickle.dump(actividades, archivo)
                
            print("Actividades guardadas correctamente.")
        except Exception as e:
            print(f"Error al guardar actividades: {e}")

    def cargar_actividades(self):
        try:
            with open(self.nombre_archivo, 'rb') as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            return []
        except EOFError:
            return []
        except Exception as e:
            print(f"Error al cargar actividades: {e}")
            return []