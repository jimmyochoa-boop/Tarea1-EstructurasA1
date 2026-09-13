"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 13 - Combinador de listas
 
Paso 1 (Entender):
    Entrada: dos o mas listas
    Proceso: alternar elementos con indices y bucles
    Salida: lista intercalada
    Ejemplo: cl.intercalar([1,2], [3,4])
    Esperado: [1, 3, 2, 4]
 
Paso 2 (Bosquejo a mano):
    lista1=[1,2]  
    lista2=[3,4]  
    largo=max(2,2)=2
    i=0: agrego lista1[0]=1, lista2[0]=3 -> resultado=[1,3]
    i=1: agrego lista1[1]=2, lista2[1]=4 -> resultado=[1,3,2,4]
 
Paso 3 (Patron):
    intercalar: usa un indice que recorre hasta el largo mayor, validando
      con if que ese indice exista en cada lista antes de usarlo
    intercalar_multiples(*listas): reutiliza intercalar de dos en dos
"""
# Paso 4 - Escribir el codigo
class CombinadorListas:
    def __init__(self):
        pass

    def intercalar(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        # reutilizo intercalar de dos en dos
        resultado = listas[0]
        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])
        return resultado

# Paso 5 - Prueba de Escritorio
cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))