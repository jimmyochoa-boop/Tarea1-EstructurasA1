"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 17 - Grupo de edades
 
Paso 1 (Entender):
    Entrada: edades en lote
    Proceso: clasificar con if/elif, agrupar en diccionario
    Salida: diccionario agrupado, promedio
    Ejemplo: ae.agrupar_por_categoria(5, 15, 30, 70)
    Esperado: {'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}
 
Paso 2 (Bosquejo a mano):
    5 -> menor a 13 -> niño
    15 -> no < 13, si < 18 -> adolescente
    30 -> no < 13 ni < 18, si < 65 -> adulto
    70 -> no cumple ninguna anterior -> mayor
 
Paso 3 (Patron):
clasificar_edad: cadena de if/elif/else segun rangos de edad
agrupar_por_categoria(*edades): reutiliza clasificar_edad y va
armando un diccionario {categoria: [edades]}
edad_promedio_categoria: busca la lista de esa categoria y calcula su promedio
"""
# Paso 4 - Escribir el codigo
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos:
            return 0
        lista_edades = self.grupos[categoria]
        return sum(lista_edades) / len(lista_edades)
    
# Paso 5 - Prueba de Escritorio
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))