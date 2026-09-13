"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 8 - Asignador de equipos
 
Paso 1 (Entender):
Entrada: nombres de equipos y jugadores
Proceso: crear estructura equipo -> [jugadores], contar, comparar
Salida: equipo con mas jugadores
Ejemplo: crear_equipo("A"), agregar_jugador("A","Juan"),
agregar_jugador("A","Pedro")
 
Paso 2 (Bosquejo a mano):
crear_equipo("A") -> {"A": []}
agregar_jugador("A","Juan") -> {"A": ["Juan"]}
agregar_jugador("A","Pedro") -> {"A": ["Juan","Pedro"]}
si hubiera un equipo "B" con 1 jugador, al comparar 2 contra 1
el metodo se queda con "A"
 
Paso 3 (Patron):
crear_equipo: inicia una lista vacia como valor en un diccionario
(diccionario de listas)
agregar_jugador: append() sobre esa lista
equipo_mayor_integrantes: recorre .items() comparando len() con
una variable auxiliar
"""
# Paso 4 - Escribir el codigo
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = None
        cantidad = -1
        for nombre, jugadores in self.equipos.items():
            if len(jugadores) > cantidad:
                cantidad = len(jugadores)
                mayor = nombre
        return mayor

# Paso 5 - Prueba de Escritorio
eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")

eq.crear_equipo("B")
eq.agregar_jugador("B", "Miguel")
print("El equipo con mayor cantidad de jugadores es: ", eq.equipo_mayor_integrantes())
