"""
Clase que se utilizara en la api de Flask para simular la entidad Tienda
"""
class Tienda():
	def __init__(self, nombre, direccion):
		self.nombre = nombre
		self.direccion = direccion
		self.productos = []

	def agregar_inventario(self, inventario):
		self.productos.append(inventario)

	def mostrar_inventario(self):
		return list(self.productos)