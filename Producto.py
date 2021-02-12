"""
Clase que se utilizara en la api de Flask para simular la entidad Producto
"""
class Producto():
	def __init__(self, id_producto, nombre, precio, sku):
		self.id_producto = id_producto
		self.nombre = nombre
		self.precio = precio
		self.sku = sku