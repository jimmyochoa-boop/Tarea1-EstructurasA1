"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 10 - Gestor de tareas con prioridad
 
Paso 1 (Entender):
Entrada: descripciones y prioridades
Proceso: guardar tuplas, filtrar por prioridad, eliminar
Salida: tareas filradas
Ejemplo: agregar_tarea("Estudiar","alta"), agregar_tarea("Leer","baja")
    -> tareas_prioritarias()
Esperado: [("Estudiar", "alta")]
 
Paso 2 (Bosquejo a mano):
lista_tareas = []
agrego ("Estudiar","alta") -> [("Estudiar","alta")]
agrego ("Leer","baja") -> [("Estudiar","alta"), ("Leer","baja")]
tareas_prioritarias(): me quedo con las que tengan tarea[1]=="alta"
resultado = [("Estudiar","alta")]
 
Paso 3 (Patron):
agregar_tarea: guarda una tupla (descripcion, prioridad) en una lista
tareas_prioritarias: recorre la lista y compara la posicion [1]
eliminar_completada: busca por descripcion y usa .remove()
"""
# Paso 4 - Escribir el codigo
class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        altas = []
        for tarea in self.lista_tareas:
            if tarea[1] == "alta":
                altas.append(tarea)
        return altas

    def eliminar_completada(self, descripcion):
        for tarea in self.lista_tareas:
            if tarea[0] == descripcion:
                self.lista_tareas.remove(tarea)
                break

# Paso 5 - Prueba de Escritorio
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())