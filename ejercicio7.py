"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 7 - Mapeador de edades
 
Paso 1 (Entender):
Entrada: nombres y edades
Proceso: guardar en diccionario, filtrar, promediar
Salida: lista filtrada, promedio
Ejemplo: agregar_persona("Ana",28), agregar_persona("Bob",17)
-> personas_mayores(18)
Esperado: ["Ana"]
 
Paso 2 (Bosquejo a mano):
diccionario = {"Ana":28, "Bob":17}
Ana: 28>=18 si entra     
Bob: 17>=18 no entra
resultado = ["Ana"]
 
Paso 3 (Patron):
agregar_persona: guarda nombre -> edad en un diccionario
personas_mayores: recorre .items() y compara con >=
edad_promedio: usa .values() y sum()/len()
"""
# Paso 4 - Escribir el codigo
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        edades = self.personas.values()
        return sum(edades) / len(edades)
    
# Paso 5 - Prueba de Escritorio
gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print("La persona con mayor edad mapeada es: ", gp.personas_mayores(18))