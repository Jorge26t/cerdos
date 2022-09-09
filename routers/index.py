from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify, session
from models.usuario import Usuario
from utils.Complemento import Complement
from datetime import date, datetime
# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
index = Blueprint('index', __name__)

# esto es el index que muestra cuando inicia el sistema
@index.route('/')
def Login():
    if 'id_usu' in session and 'id_rol' in session:
        ahora = datetime.now()
        now = Complement.current_date_format(ahora)
        return render_template('view/home/index.html', now = now)
    else:
        return render_template('Login/index.html')

# controlador del inicio de sesión
@index.route('/Ingreso', methods=['POST'])
def Ingreso():
    _usuario = request.form['usuario']
    _pass = request.form['password']
    dato = Usuario.login(_usuario, _pass)
    return jsonify(dato)

# crear sesiones de usuario
@index.route('/Crear_variable', methods=['POST'])
def Crear_variable():
    session['id_usu'] = request.form['id_usu']
    session['id_rol'] = request.form['id_rol']
    return str(1)

#vista cerar sesion
@index.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return redirect(url_for('index.Login'))

## vistas crear rol
@index.route('/vista_rol')
def vista_rol():
    return render_template('view/usuario/rol.html')

#vista listar rol
@index.route('/listar_rol')
def listar_rol():
    return render_template('view/usuario/listar_rol.html')

# vista crear usuario
@index.route('/create_user')
def create_user():
    if 'id_usu' in session and 'id_rol' in session:
        data = Usuario.Listar_rol_combo() 
    return render_template('view/usuario/crear_user.html', data = data )

#vista listar usuario
@index.route('/lista_usuario')
def lista_usuario():
    if 'id_usu' in session and 'id_rol' in session:
        data = Usuario.Listar_rol_combo()
    return render_template('view/usuario/listar_usuario.html', data = data)

#vista listar usuario
@index.route('/hacienda')
def hacienda():
    if 'id_usu' in session and 'id_rol' in session:
        data = Usuario.Traer_hacienda()
    return render_template('view/home/empresa.html', data = data)