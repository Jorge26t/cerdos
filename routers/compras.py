from flask import Blueprint, request, session
from flask import jsonify
from models.compras import Compras
import time

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
compras = Blueprint('compras', __name__)

# controlador para regitra el proveedor
@compras.route('/registrar_proveedor', methods=['POST'])
def registrar_proveedor():
    if request.method == 'POST':
        _razon_social = request.form['razon_social']
        _ruc = request.form['ruc']
        _telefonoo = request.form['telefonoo']
        _correo = request.form['correo']
        _direccion = request.form['direccion']
        _descripcion = request.form['descripcion']
        _encargdo = request.form['encargdo']
        _telefonoo_en = request.form['telefonoo_en']  

        dato = Compras.Registrar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion)
        return str(dato)

# controlador para listar el proveedor
@compras.route('/listado_proveedores', methods=['GET'])
def listado_proveedores():
    if request.method == 'GET':
        dato = Compras.Listado_proveedores()
        return jsonify(dato)

# controlador para estado del proveedor
@compras.route('/estado_proveedor', methods=['POST'])
def estado_proveedor():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Compras.Estado_proveedor(_id, _dato)
        return str(dato)

# controlador para editar el proveedor
@compras.route('/editar_proveedor', methods=['POST'])
def editar_proveedor():
    if request.method == 'POST':
        _id = request.form['id']
        _razon_social = request.form['razon_social']
        _ruc = request.form['ruc']
        _telefonoo = request.form['telefonoo']
        _correo = request.form['correo']
        _direccion = request.form['direccion']
        _descripcion = request.form['descripcion']
        _encargdo = request.form['encargdo']
        _telefonoo_en = request.form['telefonoo_en']  

        dato = Compras.Editar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion, _id)
        return str(dato)

# controlador para registrar la compra
@compras.route('/registrar_compra_alimento', methods=['POST'])
def registrar_compra_alimento():
    if request.method == 'POST':
        _id = session['id_usu']
        _id_pro = request.form['proveedor']
        _fecha_c = request.form['fecha_c']
        _numero_compra = request.form['numero_compra']
        _tipo_comprobante = request.form['tipo_comprobante']
        _iva = request.form['iva']
        _subtotal = request.form['subtotal']
        _impuesto_sub = request.form['impuesto_sub']
        _total_pagar = request.form['total_pagar'] 

        dato = Compras.Registrar_compra_alimento(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id)
        return str(dato)

# controlador para registra el detalle de compra del alimento
@compras.route('/registrar_detalle_compra_alimento', methods=['POST'])
def registrar_detalle_compra_alimento():
    if request.method == 'POST':

        _id = request.form['id']
        _ida = request.form['ida']
        _precio = request.form['precio']
        _cantidad = request.form['cantidad'] 
        _descuento = request.form['descuento'] 
        _total = request.form['total'] 

        ida = _ida.split(",")
        precio = _precio.split(",")
        cantidad = _cantidad.split(",") 
        descuento = _descuento.split(",")
        total = _total.split(",") 

        for valor in zip(ida, precio, cantidad, descuento, total):
            dato = Compras.Registrar_detalle_compra_alimento(_id, valor[0], valor[1], valor[2], valor[3], valor[4])  
        return jsonify(dato)

# controlador para anular la compra de alimentos
@compras.route('/compra_alimneto_anular', methods=['POST'])
def compra_alimneto_anular():    
    if request.method == 'POST':
        _id = request.form['id']   
        dato = Compras.Anular_compra_alimentos(_id)  
        print(dato)
        return str(dato)