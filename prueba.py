#Entidad tienda
class Tienda():
	def __init__(self, nombre, direccion):
		self.nombre = nombre
		self.direccion = direccion
		self.productos = []

"""
Método para agregar/asociar un inventario a una Tienda
Argumentos:
    inventario: (dict o list) inventario para la tienda

Ejemplo:
    Tienda.agregar_inventario(inventario_tienda1)
"""
	def agregar_inventario(self, inventario):
		self.productos.append(inventario)

    #Este método retorna una lista con inventarios de productos
	def mostrar_inventario(self):
		return list(self.productos)

#Entidad Producto
class Producto():
	def __init__(self, id_producto, nombre, precio, sku):
		self.id_producto = id_producto
		self.nombre = nombre
		self.precio = precio
		self.sku = sku

#Entidad Inventario
class Inventario():
	def __init__(self, id_inventario):
		self.id_inventario = id_inventario
		self.inventario = {}
		self.stock = 0

"""
Método que sirve para agregar un producto a un diccionario "inventario"
Argumentos:
    id_producto : (string) ID con el que se identifica el producto
    nombre_producto: (string) Nombre del producto
    stock: (int) El número de productos que se pasan al inventario

Ejemplo:
    Inventario.agregar_producto("008", "tennis", 50)
"""
    def agregar_producto(self, id_producto, nombre_producto, stock):
		self.inventario = {"id_producto":id_producto, "nombre_producto":nombre_producto, "stock":stock}

    #Método para retornar el diccionario que se va a agregar a la entidad Tienda
	def regresar_inventario(self):
		return self.inventario

"""
Método dónde se verifica si hay suficientes productos para retirar, si no hay suficientes se lanza un mensaje de error

Argumentos:
    inv: (dict o list) Inventario al que se le quiere retirar el producto
    cant: (int) Cantidad de producto que se quiere retirar
    
Ejemplo:
    Inventario.retirar_producto(inventario_tienda1, 20)
"""
	def retirar_producto(self, inv, nom, cant):
		if inv['stock'] < cant:
		    print('No hay suficiente stock')
		else:
			inv["stock"] = inv['stock'] - cant


#Main

#Se crea un producto
producto1 = Producto("001", "p1", 15.99, "12532")

#Se crea un inventario y se agregan los productos anteriormente creados
inventario = Inventario("inv1")
inventario.agregar_producto(producto1.id_producto, producto1.nombre, 40)


#Se imprime dicho inventario
inventario_tienda1 = inventario.regresar_inventario()
print(inventario_tienda1)

#Se retira del inventario la cantidad de 20 productos "p3"
inventario.retirar_producto(inventario_tienda1, "p3", 20)

#Se imprime dicho inventario para confirmar el retiro
inventario_tienda1 = inventario.regresar_inventario()
print(inventario_tienda1)

#Se crea la tienda y se le agrega el inventario
tienda1 = Tienda("nombre1", "direccion1")
tienda1.agregar_inventario(inventario_tienda1)
most = tienda1.mostrar_inventario()
print(most)
print("Se ingresó exitosamente el inventario")

