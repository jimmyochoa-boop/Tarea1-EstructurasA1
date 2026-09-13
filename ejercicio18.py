"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 18 - Matriz de distancias
 
Paso 1 (Entender):
Entrada: tuplas (x, y) como puntos
Proceso: calcular distancia con formula, comparar, guardar
Salida: distancia numerica, punto mas cercano
Ejemplo: cd.distancia_euclidiana((0,0), (3,4))
Esperado: 5.0
 
Paso 2 (Bosquejo a mano):
p1=(0,0)  
p2=(3,4)
dx=0-3=-3   
dy=0-4=-4
distancia = raiz((-3)^2+(-4)^2) = raiz(9+16) = raiz(25) = 5.0
 
Paso 3 (Patron):
distancia_euclidiana: aplica la formula usando [0] y [1] de cada
tupla, y guarda el resultado en una lista de distancias
punto_mas_cercano(referencia,*puntos): reutiliza distancia_euclidiana
    y se queda con el punto de menor distancia
"""
# Paso 4 - Escribir el codigo
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        cercano = None
        menor_distancia = None
        for punto in puntos:
            d = self.distancia_euclidiana(referencia, punto)
            if menor_distancia is None or d < menor_distancia:
                menor_distancia = d
                cercano = punto
        return cercano
    
# Paso 5 - Prueba de Escritorio
cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))