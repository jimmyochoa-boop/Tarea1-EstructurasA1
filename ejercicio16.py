"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 16 - Codificador Cesar
 
Paso 1 (Entender):
    Entrada: letra/palabra y desplazamiento (1-25)
    Proceso: convertir a codigo ASCII, desplazar con %, guardar historial
    Salida: palabra codificada
    Ejemplo: cc.codificar_palabra("hola", 3)
 
Paso 2 (Bosquejo a mano):
    h -> posicion 7 (a=0) + 3 = 10 -> k
    o -> posicion 14 + 3 = 17 -> r
    l -> posicion 11 + 3 = 14 -> o
    a -> posicion 0 + 3 = 3 -> d
    resultado = "krod"
 
Paso 3 (Patron):
    codificar_letra: usa ord() para pasar la letra a numero, resta la
      base ('a' o 'A'), suma el desplazamiento y aplica %26 para no
      salirse del abecedario, luego chr() la vuelve a convertir en letra
    codificar_palabra: reutiliza codificar_letra para cada caracter y
      guarda la palabra original y la codificada en un diccionario
"""
# Paso 4 - Escribir el codigo
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        base = ord('A') if letra.isupper() else ord('a')
        nueva = (ord(letra) - base + desplazamiento) % 26 + base
        return chr(nueva)

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = codificada
        return codificada
    
# Paso 5 - Prueba de Escritorio
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))