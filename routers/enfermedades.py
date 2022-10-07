from flask import Blueprint, request, session
from flask import jsonify
from models.enfermedad import Enfermedad  
import time

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
enfermedad = Blueprint('enfermedad', __name__)

# controlador para crear el veterinrio
@enfermedad.route('/registrar_veterinario', methods=['POST'])
def registrar_veterinario():
    if request.method == 'POST':
        _nombre = request.form['nombre']
        _apellido = request.form['apellido']
        _numero_doc = request.form['numero_doc']
        _telefono = request.form['telefono']
        _direccion = request.form['direccion']
        _sucursal = request.form['sucursal']  
        
        dato = Enfermedad.Registrar_veterinario(_nombre, _apellido, _numero_doc, _telefono, _direccion, _sucursal)
        return str(dato)

# controlador para listar el veterinario
@enfermedad.route('/listar_veterinario', methods=['GET'])
def listar_veterinario():
    if request.method == 'GET':
        dato = Enfermedad.Listar_veterinario()
        return jsonify(dato)

# controlador para estado del veterinario
@enfermedad.route('/estado_veterinario', methods=['POST'])
def estado_veterinario():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Enfermedad.Estado_veterinario(_id,_dato)
        return str(dato)

# controlador para editar el veterinrio
@enfermedad.route('/editarr_veterinario', methods=['POST'])
def editarr_veterinario():
    if request.method == 'POST':
        _id = request.form['id']
        _nombre = request.form['nombre']
        _apellido = request.form['apellido']
        _numero_doc = request.form['numero_doc']
        _telefono = request.form['telefono']
        _direccion = request.form['direccion']
        _sucursal = request.form['sucursal']  
        
        dato = Enfermedad.Editar_veterinario(_nombre, _apellido, _numero_doc, _telefono, _direccion, _sucursal, _id)
        return str(dato)

# controlador para crear la enfermedad
@enfermedad.route('/registrar_tipo_enfermedad', methods=['POST'])
def registrar_tipo_enfermedad():
    if request.method == 'POST':
        _nombre = request.form['nombre']
        _descripcion = request.form['descripcion']  
        
        dato = Enfermedad.Registrar_tipo_enfermedad(_nombre, _descripcion)
        return str(dato)

# controlador para listar el veterinario
@enfermedad.route('/listar_enfermedad', methods=['GET'])
def listar_enfermedad():
    if request.method == 'GET':
        dato = Enfermedad.Listar_enfermedad()
        return jsonify(dato)

# controlador para estado de la enfermedad
@enfermedad.route('/estado_enfermedad', methods=['POST'])
def estado_enfermedad():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Enfermedad.Estado_enfermedad(_id,_dato)
        return str(dato)
    
# controlador para editar la enfermedad
@enfermedad.route('/editar_tipo_enfermedad', methods=['POST'])
def editar_tipo_enfermedad():
    if request.method == 'POST':
        _id = request.form['id']
        _nombre = request.form['nombre']
        _descripcion = request.form['descripcion']  
        
        dato = Enfermedad.Editar_tipo_enfermedad(_nombre, _descripcion, _id)
        return str(dato)

# controlador para crear el tipo de tratamiento
@enfermedad.route('/registrar_tipo_tratamiento', methods=['POST'])
def registrar_tipo_tratamiento():
    if request.method == 'POST':
        _nombre = request.form['nombre']
        _descripcion = request.form['descripcion']  
        
        dato = Enfermedad.Registrar_tipo_tratamiento(_nombre, _descripcion)
        return str(dato)

# controlador para listar el tipo tratamiento
@enfermedad.route('/listar_tipo_tratamiento', methods=['GET'])
def listar_tipo_tratamiento():
    if request.method == 'GET':
        dato = Enfermedad.Listar_tipo_tratamiento()
        return jsonify(dato)

# controlador para estado de la enfermedad
@enfermedad.route('/estado_tipo_tratamiento', methods=['POST'])
def estado_tipo_tratamiento():
    if request.method == 'POST':
        _id = request.form['id']
        _dato = request.form['dato']
        dato = Enfermedad.Estado_tipo_tratamiento(_id,_dato)
        return str(dato)
 
 # controlador para editar el tipo de tratamiento
@enfermedad.route('/editar_tipo_tratamiento', methods=['POST'])
def editar_tipo_tratamiento():
    if request.method == 'POST':
        _id = request.form['id']
        _nombre = request.form['nombre']
        _descripcion = request.form['descripcion']  
        
        dato = Enfermedad.Editar_tipo_tratamiento(_nombre, _descripcion, _id)
        return str(dato)
