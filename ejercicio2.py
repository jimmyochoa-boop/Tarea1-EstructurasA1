"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 2 - Contador de palabras unicas
 
Paso 1 - Entender:
Entrada: palabras individuales o en lote
Proceso: guardar en un conjunto y en una lista
Salida: cantidad de palabras unicas
Ejemplo: at.agregar_multiples("hola","mundo","hola") -> contar_palabras()
Esperado: 2
 
Paso 2 - Bosquejo a mano:
agrego "ok" -> conjunto {ok}         
agrego "datos" -> conjunto {ok, datos}   
agrego "ok" otra vez -> conjunto no cambia   
lista [ok, ok, datos]
contar_palabras() = len(conjunto) = 2
 
Paso 3 (Patron):
agregar_palabra: set.add() ignora duplicados solo
agregar_multiples(*args): reutiliza agregar_palabra en un bucle
"""


# Paso 4 - Escribir el codigo
class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

# Paso 5 - Prueba de Escritorio
            
at = AnalizadorTexto()
at.agregar_multiples("ok", "ok", "datos")
print("Tiene", at.contar_palabras(), "palabras unicas")