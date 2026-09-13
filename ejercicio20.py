"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 20 - Analizador de patrones en textos
 
Paso 1 (Entender):
Entrada: texto y patron de busqueda
Proceso: split(), filtrar, agrupar por longitud, quitar duplicados
Salida: listas, diccionario, conjunto
Ejemplo: ap.agrupar_por_longitud("el gato esta aqui")
Esperado: {2:['el'], 4:['gato','esta','aqui']}
 
Paso 2 (Bosquejo a mano):
split() -> ["el","gato","esta","aqui"]
"el" largo 2   
"gato" largo 4   
"esta" largo 4   
"aqui" largo 4
grupos = {2:["el"], 4:["gato","esta","aqui"]}
 
Paso 3 (Patron):
encontrar_palabras: split() + startswith() para filtrar
agrupar_por_longitud: reutiliza split() y agrupa con len() de clave
palabras_unicas: convierte la lista del ultimo texto en un set
"""
# Paso 4 - Escribir el codigo
class AnalizadorPatrones:
    def __init__(self):
        self.ultimo_texto = ""

    def encontrar_palabras(self, texto, patron):
        self.ultimo_texto = texto
        palabras = texto.split()
        encontradas = []
        for palabra in palabras:
            if palabra.startswith(patron):
                encontradas.append(palabra)
        return encontradas

    def agrupar_por_longitud(self, texto):
        self.ultimo_texto = texto
        palabras = texto.split()
        grupos = {}
        for palabra in palabras:
            largo = len(palabra)
            if largo not in grupos:
                grupos[largo] = []
            grupos[largo].append(palabra)
        return grupos

    def palabras_unicas(self):
        palabras = self.ultimo_texto.split()
        return set(palabras)

# Paso 5 - Prueba de Escritorio
ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato esta aqui"))