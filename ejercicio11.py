"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 11 - Contador de frecuencia
 
Paso 1 (Entender):
Entrada: elementos individuales o en lote
Proceso: guardar en diccionario, contar, encontrar maximo
Salida: elemento mas frecuente y su conteo
Ejemplo: agregar_elemento("a"), agregar_elemento("b"),
agregar_elemento("a") -> elemento_mas_frecuente()
Esperado: "a"
 
Paso 2 (Bosquejo a mano):
frecuencias = {}
agrego "a": no estaba -> {"a":1}
agrego "b": no estaba -> {"a":1,"b":1}
agrego "a": ya estaba -> {"a":2,"b":1}
"a" tiene el valor mas alto (2) -> elemento_mas_frecuente() = "a"
 
Paso 3 (Patron):
agregar_elemento: patron de "diccionario como contador"
elemento_mas_frecuente: recorre .items() comparando con una variable
auxiliar
frecuencia_elemento: consulta directa en el diccionario
"""
# Paso 4 - Escribir el codigo
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        mas_frecuente = None
        maximo = 0
        for elemento, veces in self.frecuencias.items():
            if veces > maximo:
                maximo = veces
                mas_frecuente = elemento
        return mas_frecuente

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        return 0
    
# Paso 5 - Prueba de Escritorio
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print("El elemento mas frecuente es: ",cf.elemento_mas_frecuente())