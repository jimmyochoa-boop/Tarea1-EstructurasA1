"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 15 - Divisores de un numero
 
Paso 1 (Entender):
    Entrada: uno o varios numeros
    Proceso: encontrar divisores con bucles, verificar suma
    Salida: tuplas, booleano, diccionario
    Ejemplo: df.encontrar_divisores(12)
    Esperado: (1, 2, 3, 4, 6, 12)
 
Paso 2 (Bosquejo a mano):
    12%1=0 12%2=0 12%3=0 12%4=0 12%5=2(no) 12%6=0
    divisores = (1,2,3,4,6,12)
    es_perfecto(12)? suma sin el 12: 1+2+3+4+6=16, 16 != 12 -> False
 
Paso 3 (Patron):
    encontrar_divisores: recorre desde 1 hasta el numero probando modulo
    es_perfecto: reutiliza encontrar_divisores y compara la suma con ==
    encontrar_multiples_divisores(*numeros): reutiliza encontrar_divisores
      para cada numero y arma un diccionario {numero: tupla_divisores}
"""
# Paso 4 - Escribir el codigo
class DivisorFinder:
    def __init__(self):
        pass

    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for d in divisores:
            if d != numero:
                suma += d
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)
        return resultado
    
# Paso 5 - Prueba de Escritorio
df = DivisorFinder()
print("Los divisores son: ", df.encontrar_divisores(12))