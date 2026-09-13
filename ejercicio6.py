"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 6 - Estadisticas de temperatura
 
Paso 1 (Entender):
Entrada: temperaturas individuales o en lote
Proceso: guardar, calcular minima, maxima y promedio
Salida: valores estadisticos
Ejemplo: gt.registrar_multiples(20,25,18,30) -> gt.promedio()
Esperado: 23.25
 
Paso 2 (Bosquejo a mano):
lista = [20,25,18,30]
minima=18   
maxima=30
promedio = (20+25+18+30)/4 = 93/4 = 23.25
 
Paso 3 (Patron):
registrar_temperatura: append() a la lista
registrar_multiples(*temps): reutiliza registrar_temperatura
minima/maxima: funciones built-in min() y max()
promedio: sum()/len()
"""
# Paso 4 - Escribir el codigo
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for t in temps:
            self.registrar_temperatura(t)
            
# Paso 5 - Prueba de Escritorio
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print("El Promedio del gestor de las temperaturas es", gt.promedio())