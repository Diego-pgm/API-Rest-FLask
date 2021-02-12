"""
Clase que se utilizara en la api de Flask para simular la entidad inventario

Se crea esta clase para facilitar la union entre la tabla tiendas y 
la tabla productos y tener un mejor manejo del programa
"""
class Inventario():
	def __init__(self, id_inventario):
		self.id_inventario = id_inventario
		self.inventario = {}
		self.stock = 0

	def agregar_producto(self, id_producto, nombre_producto, stock):
		self.inventario = {"id_producto":id_producto, "nombre_producto":nombre_producto, "stock":stock}

	def regresar_inventario(self):
		return self.inventario

	def retirar_producto(self, inv, cant): 
		if inv['stock'] < cant:
			print('No hay suficiente stock')
		else:
			inv["stock"] = inv['stock'] - cant
