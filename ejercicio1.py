""" 
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 1 - Validador de notas con promedio

Paso 1 (Entender):
Entrada: notas individuales o en lote (*args).
Proceso: validar cada nota entre 0 y 100, guardar las validas en una lista.
Salida: True/False, lista de validas, promedio.

Paso 2 (Bosquejo a mano):
85 valida? si       
92 valida? si        
110 valida? no porque es > 100
78 valida? si       -
5 valida? no porque < 0   
88 valida? si
lista de validas: [85, 92, 78, 88]
promedio = (85+92+78+88)/4 = 343/4 = 85.7

Paso 3 (Patron):
validar_nota(nota): validador simple con if y operadores relacionales
cargar_notas(*args): recibe varias notas en un tuple y se reutitiza
validar_nota para quedarse solo con las que sirven
notas (atributo): lista que va creciendo, arranca vacia en __init__"""

# Paso 4 - Escribir el codigo
class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    
# Paso 5 - Prueba de Escritorio
c = Calificador()
c.cargar_notas(85, 92, 110, 78, -5, 88)
print(c.notas, "y el promedio final es", c.promedio())