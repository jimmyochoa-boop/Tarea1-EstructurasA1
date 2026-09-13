"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 5 - Detector de numeros pares e impares
 
Paso 1 (Entender):
Entrada: numeros en lote
Proceso: clasificar pares/impares con el operador %
Salida: diccionario y tupla con cantidades
Ejemplo: an.separar(1,2,3,4,5)
Esperado: {'pares':[2,4], 'impares':[1,3,5]}
 
Paso 2 (Bosquejo a mano):
1%2=1 impar   
2%2=0 par   
3%2=1 impar   
4%2=0 par   
5%2=1 impar
pares=[2,4]   
impares=[1,3,5]
cantidad_pares_impares() = (2, 3)
 
Paso 3 (Patron):
es_par: usa el operador modulo
separar(*numeros): reutiliza es_par y clasifica en dos listas
guardadas dentro de un diccionario
cantidad_pares_impares: arma una tupla con el len() de cada lista
"""
# Paso 4 - Escribir el codigo
class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        return False

    def separar(self, *numeros):
        for n in numeros:
            if self.es_par(n):
                self.pares.append(n)
            else:
                self.impares.append(n)
        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))

# Paso 5 - Prueba de Escritorio
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))