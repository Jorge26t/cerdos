from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify, session

from models.usuario import Usuario
from models.cerdo import Cerdo
from models.galpon import Galpon 

from utils.Complemento import Complement
from datetime import date, datetime
import random

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
index = Blueprint('index', __name__)

# esto es el index que muestra cuando inicia el sistema
@index.route('/')
def Index():
    return render_template('Web/index.html')

# esto es el login que muestra cuando inicia el sistema
@index.route('/Login')
def Login():
    if 'id_usu' in session and 'id_rol' in session:
        return redirect(url_for('index.Admin'))
    else:
        return render_template('Login/index.html')

# esto es el Admin que muestra cuando inicia el sistema
@index.route('/Admin')
def Admin():
    if 'id_usu' in session and 'id_rol' in session:
        ahora = datetime.now()
        now = Complement.current_date_format(ahora)
        return render_template('view/home/index.html', now = now)
    else:
        return redirect(url_for('index.Login'))

#vista pagina web
@index.route('/pag_web')
def pag_web(): 
    return render_template('view/home/pag_web.html')

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

#vista de razas
@index.route('razas')
def razas():
    return  render_template('view/cerdo/razas.html')

#vista crear cerdos
@index.route('/new_cerdo')
def new_cerdo():
    if 'id_usu' in session and 'id_rol' in session:
        data = Cerdo.Traer_razas_combo()
        codigo = random.randint(0, 999999999)
    return render_template('view/cerdo/registro_cerdo.html', data = data, codigo = codigo)

#vista listar cerdo
@index.route('/list_cerdo')
def list_cerdo():
    data = Cerdo.Traer_razas_combo()
    return render_template('view/cerdo/listado_cerdos.html',  data = data)

#vista crear galpón
@index.route('/create_galpon')
def create_galpon(): 
    data = Galpon.Traer_tipo_galpon_combo()
    return render_template('view/galpon/new_galpon.html', data = data)

#vista listar el galpón
@index.route('/list_galpon')
def list_galpon(): 
    data = Galpon.Traer_tipo_galpon_combo()
    return render_template('view/galpon/list_galpon.html', data = data)

#vista tipo de galpon
@index.route('/tipo_galpon')
def tipo_galpon(): 
    return render_template('view/galpon/tipo_galpon.html')

#vista del galpon del cerdo
@index.route('/list_galpon_cerdo')
def list_galpon_cerdo(): 
    data = Galpon.Listar_cerdo_galpon_LIST()
    return render_template('view/galpon/list_galpon_cerdo.html', data = data)

#crear galpon cerdo
@index.route('/create_galpon_cerdo')
def create_galpon_cerdo(): 
    data = Galpon.Listar_galpon_combo()
    return render_template('view/galpon/create_galpon_cerdo.html', data = data)

