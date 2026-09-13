"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 9 - Validador de caracteres
 
Paso 1 (Entender):
    Entrada: textos para analizar
    Proceso: recorrer caracter por caracter y clasificar
    Salida: diccionario con conteos
    Ejemplo: astr.contar_por_tipo("Hola123")
    Esperado: {'vocales':2, 'consonantes':2, 'digitos':3}
 
Paso 2 (Bosquejo a mano):
    H consonante   
    o vocal   
    l consonante   
    a vocal   
    1,2,3 digitos
    vocales=2 (o,a)  
    consonantes=2 (H,l)  
    digitos=3 (1,2,3)
 
Paso 3 (Patron):
    solo_vocales: revisa si el caracter esta en "aeiouAEIOU"
    contar_por_tipo: recorre el texto con for, usa isdigit()/isalpha()
      y reutiliza solo_vocales para separar vocal de consonante
    el atributo del texto mas largo se actualiza comparando len()
"""
# Paso 4 - Escribir el codigo
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        vocales = "aeiouAEIOU"
        if letra in vocales:
            return True
        return False

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteo = {"vocales": 0, "consonantes": 0, "digitos": 0}
        for caracter in texto:
            if caracter.isdigit():
                conteo["digitos"] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    conteo["vocales"] += 1
                else:
                    conteo["consonantes"] += 1
        return conteo

# Paso 5 - Prueba de Escritorio
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))