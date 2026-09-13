"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 12 - Selector de rango con tuplas
 
Paso 1 (Entender):
    Entrada: pares (inicio, fin) para varios rangos
    Proceso: crear rangos como tuplas, unir sin duplicados
    Salida: lista de elementos unicos
    Ejemplo: sr.elementos_en_multiples_rangos((1,3), (2,4))
    Esperado: [1, 2, 3, 4]
 
Paso 2 (Bosquejo a mano):
    rango (1,3) -> (1,2,3)      
    rango (2,4) -> (2,3,4)
    conjunto_final = {}
    agrego 1,2,3 -> {1,2,3}
    agrego 2,3,4 -> 2 y 3 ya estaban solo se suma el 4 -> {1,2,3,4}
 
Paso 3 (Patron):
    crear_rango: arma una tupla usando range()
    elementos_en_multiples_rangos(*rangos): reutiliza crear_rango y usa
      un conjunto para que no se repitan numeros entre rangos
"""
# Paso 4 - Escribir el codigo
class SelectorRango:
    def __init__(self):
        pass

    def crear_rango(self, inicio, fin):
        numeros = []
        for n in range(inicio, fin + 1):
            numeros.append(n)
        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        conjunto_final = set()
        for r in rangos:
            inicio = r[0]
            fin = r[1]
            rango_tupla = self.crear_rango(inicio, fin)
            for numero in rango_tupla:
                conjunto_final.add(numero)
        return list(conjunto_final)
    
# Paso 5 - Prueba de Escritorio
sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))