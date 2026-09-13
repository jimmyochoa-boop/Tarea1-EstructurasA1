"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 4 - Inversor de secuencias
 
Paso 1 (Entender):
Entrada: una o varias listas
Proceso: invertir manualmente con bucle (sin reversed()), guardar en dict
Salida: lista invertida o diccionario
Ejemplo: inv.invertir_lista([1,2,3])
Esperado: [3, 2, 1]
 
Paso 2 (Bosquejo a mano):
lista=[1,2,3] indices 0,1,2
recorro desde el ultimo indice hacia el primero:
i=2 -> tomo lista[2]=3 -> invertida=[3]
i=1 -> tomo lista[1]=2 -> invertida=[3,2]
i=0 -> tomo lista[0]=1 -> invertida=[3,2,1]
 
Paso 3 (Patron):
invertir_lista: for con range() hacia atras, sin metodos listos
invertir_multiples(*listas): reutiliza invertir_lista y guarda el
resultado en un diccionario usando tuple(lista) como clave, porque
una lista no se puede usar de clave (no es hashable)
"""
# Paso 4 - Escribir el codigo
class InversorSecuencia:
    def __init__(self):
        self.historial = {}

    def invertir_lista(self, lista):
        # la invierto a mano, sin usar reversed() ni lista[::-1]
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        for lista in listas:
            inv = self.invertir_lista(lista)
            self.historial[tuple(lista)] = inv
        return self.historial
    
# Paso 5 - Prueba de Escritorio
inv = InversorSecuencia()
print("El inverso es", inv.invertir_lista([1, 2, 3]))