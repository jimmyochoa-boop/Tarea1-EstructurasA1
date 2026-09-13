"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 3 - Gestor de compras con totales
 
Paso 1 (Entender):
Entrada: nombres de articulos y precios
Proceso: guardar en diccionario, sumar valores, filtrar por rango
Salida: total, articulos dentro de un rango
Ejemplo: agregar_articulo("pan",2.50), agregar_articulo("leche",3.00)
-> total_carrito()
Esperado: 5.50
 
Paso 2 (Bosquejo a mano):
diccionario vacio {}
agrego pan:2.50 -> {"pan":2.50}
agrego leche:3.00 -> {"pan":2.50, "leche":3.00}
total = 2.50 + 3.00 = 5.50
 
Paso 3 (Patron):
agregar_articulo: guarda clave-valor (nombre -> precio)
total_carrito: recorre .values() y suma
articulos_por_rango: recorre .items() y compara con precio_min/max
"""
# Paso 4 - Escribir el codigo
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = 0
        for precio in self.articulos.values():
            total += precio
        return total

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)
        return resultado

# Paso 5 - Prueba de Escritorio
carro = CarroCompras()
carro.agregar_articulo("pan", 2.50)
carro.agregar_articulo("leche", 3.00)
print("El total dentro a pagar es", carro.total_carrito())