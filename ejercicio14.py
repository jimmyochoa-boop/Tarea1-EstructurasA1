"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 14 - Mapeo de estudiantes a notas
 
Paso 1 (Entender):
    Entrada: estudiante -> nota
    Proceso: guardar diccionario, iterar con items(), comparar
    Salida: listas filtradas, tupla (nombre, nota)
    Ejemplo: registrar("Ana",95), registrar("Bob",70) -> mejor_estudiante()
    Esperado: ("Ana", 95)
 
Paso 2 (Bosquejo a mano):
    notas = {"Ana":95, "Bob":70}
    mejor_nota=-1  mejor_nombre=None
    Ana: 95>-1 -> mejor_nota=95, mejor_nombre="Ana"
    Bob: 70>95? no
    resultado = ("Ana", 95)
 
Paso 3 (Patron):
    registrar: guarda estudiante -> nota en un diccionario
    estudiantes_aprobados: recorre .items() y filtra con >=
    mejor_estudiante: recorre .items() comparando con variables auxiliares
      y al final arma una tupla (nombre, nota)
"""
# Paso 4 - Escribir el codigo
class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados

    def mejor_estudiante(self):
        mejor_nombre = None
        mejor_nota = -1
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return (mejor_nombre, mejor_nota)
    
# Paso 5 - Prueba de Escritorio
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print("La mejor estudiante fue ", rn.mejor_estudiante())