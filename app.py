from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask import request, render_template, redirect, url_for
import Tienda
import Inventario
import Producto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/inventarios' #Link a la BD PostgreSQL inventario
db = SQLAlchemy(app)

#Se crea la tabla Tienda 
class Tiendas(db.Model):
    __tablename__ = 'tiendas'
    id_tienda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_tienda = db.Column(db.String, unique=True)
    dir_tienda = db.Column(db.String, unique=True)
    id_inventario = db.Column(db.Integer, unique=True)

    def __init__(self, nombre_tienda, dir_tienda, id_inventario):
        self.nombre_tienda = nombre_tienda
        self.dir_tienda = dir_tienda
        self.inventario = inventario

#Se crea la tabla Productos
class Productos(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.String, primary_key=True)
    nombre_producto = db.Column(db.String)
    precio = db.Column(db.Integer)
    sku = db.Column(db.String)


    def __init__(self, id_producto, nombre_producto, precio, sku):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.sku = sku

#Se crea la tabla Inventarios
class Inventarios(db.Model):
    __tablename__ = 'inventarios'
    id_inventario = db.Column(db.Integer, db.ForeignKey(Tiendas.id_inventario),primary_key=True)
    id_producto = db.Column(db.String, db.ForeignKey(Productos.id_producto))

    def __init__(self, id_inventario):
        self.id_inventario = id_inventario
        self.inventario = {}
        self.stock = 0


db.create_all()

#Se crea el index de la API
@app.route('/index')
def index():
    return render_template('index.html')

#URL donde se muestran todas las tiendas en la tabla Tiendas en la BD
@app.route('/ver_tiendas')
def ver_tiendas():
    tiendas = Tiendas.query.all()
    return render_template('ver_tiendas.html', tiendas=tiendas)

#URL donde se muestran todos los inventarios de la tabla Inventarios en la BD 
@app.route('/ver_inventarios')
def ver_inventarios():
    inventarios = Inventarios.query.all()
    return render_template('ver_inventarios.html', inventarios=inventarios)

#URL donde se muestra todos los productos en la tabla Productos en la BD 
@app.route('/ver_productos')
def ver_productos():
    inventarios = Inventarios.query.all()
    return render_template('ver_productos.html', inventarios=inventarios)


#Se usa el método post con la URL /ver_tiendas para agregar tiendas a la BD y asociarlas a un inventario
@app.route('/agregar_tienda', methods=['POST'])
def agregar_tienda():
    inventario = Inventario.Inventario(request.form['id_inventario'])
    tienda = Tienda.Tienda(request.form['nombre_tienda'], request.form['dir_tienda'])
    tienda.agregar_inventario(inventario)
    inv1 = tienda.mostrar_inventario() 
    tienda_db = Tiendas(nombre_tienda=tienda.nombre, dir_tienda=tienda.direccion, inventario=tienda.mostrar_inventario)
    db.session.add(tienda_db)
    db.session.commit()
    return redirect(url_for('index'))

#Se usa el método post con la URL /ver_inventarios para agregar inventarios a la BD Inventarios
@app.route('/agregar_inventario', methods=['POST'])
def agregar_inventario():
    producto = Producto.Producto(request.form['id_producto'], request.form['nombre'], request.form['stock'])
    inventario = Inventario.Inventario(request.form['id_inventario'])
    inventario.agregar_producto(producto.id_producto, producto.nombre, producto.stock)
    inventario_db = Inventarios(id_inventario=inventario.id_inventario, id_tienda=request.form['id_tienda'])
    db.session.add(inventario_db)
    db.session.commit()
    return redirect(url_for('index'))

#Se usa el método post con la URL /ver_productos para agregar productos a la BD Productos 
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    producto = Producto.Producto(request.form['id_producto'], request.form['nombre'], request.form['precio'], request.form['sku'])
    inventario = Inventario.Inventario(request.form['id_inventario'])
    inventario.agregar_producto(producto.id_producto, producto.nombre, int(request.form['stock']))
    inv = inventario.regresar_inventario()
    print(inv)
    inventario.retirar_producto(inv, 30)
    inv = inventario.regresar_inventario()
    print(inv)
    producto_db = Productos(id_producto=producto.id_producto, nombre_producto=producto.nombre, precio=producto.precio, sku=producto.sku)
    db.session.add(producto_db)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True) 




