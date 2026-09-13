"""
Nombre: Jimmy Ochoa
Curso: A1 - 3er Semestre
Materia: Estructura de Datos

Ej 19 - Inventario de productos
 
Paso 1 (Entender):
Entrada: productos y cantidades
Proceso: guardar/actualizar diccionario, validar, filtrar
Salida: True/False, lista de productos
Ejemplo: agregar_stock("pan",50), restar_stock("pan",30),
    productos_bajo_stock(15)
 
Paso 2 (Bosquejo a mano):
stock={}
agregar_stock("pan",50) -> {"pan":50}
restar_stock("pan",30): 50>=30 si hay suficiente -> {"pan":20}, True
productos_bajo_stock(15): 20<15? no -> lista vacia []
 
Paso 3 (Patron):
agregar_stock: si existe suma, si no lo crea (patron contador)
restar_stock: valida cantidad suficiente antes de restar
productos_bajo_stock: recorre .items() y filtra por el minimo
"""
# Paso 4 - Escribir el codigo
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        bajos = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                bajos.append(producto)
        return bajos
    
# Paso 5 - Prueba de Escritorio
invt = Inventario()
invt.agregar_stock("pan", 50)
invt.restar_stock("pan", 30)
print("Ej19 ->", invt.productos_bajo_stock(25))