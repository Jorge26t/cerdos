from webbrowser import Galeon
from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify, session

from models.alimento import Alimento
from models.usuario import Usuario
from models.cerdo import Cerdo
from models.galpon import Galpon 
from models.compras import Compras 
from models.web import Web  

from utils.Complemento import Complement
from datetime import datetime
import random

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
index = Blueprint('index', __name__)

# esto es el index que muestra cuando inicia el sistema
@index.route('/')
def Index():
    dato = Web.Traer_datos_web()   
    return render_template('Web/index.html', dato = dato)

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
    dato = Web.Traer_datos_web()
    return render_template('view/home/pag_web.html', dato = dato)

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

#ver los cerdos del galpon
@index.route('/ver_cerdos_galpo/<int:id>')
def ver_cerdos_galpo(id): 
    data = Galpon.Listar_galpon_combo()
    cerdos = Galpon.Listar_cerdos_galpon_tabla(id)
    dicc = {
        'data': data,
        'cerdos': cerdos,
        'id': id
    }
    return render_template('view/galpon/cerdos_galpo.html', dicc = dicc)

#ver los cerdos del galpon por ajax
@index.route('/cedos_galpon', methods=['POST'])
def cedos_galpon(): 
    id = request.form['id'] 
    data = Galpon.Listar_cerdos_galpon(id) 
    return jsonify(data)

#vista movimientos de cerdos de galpones
@index.route('/movimientos_cerdo')
def movimientos_cerdo():  
    cerdos = Galpon.Movimientos_cerdo()
    dicc = { 
        'cerdos': cerdos
    }
    return render_template('view/galpon/movimientos_cerdo.html', dicc = dicc)

#vista movimientos de cerdos de galpones por fechas
@index.route('/movimientos_cerdo_fecha/<string:f_i>/<string:f_f>')
def movimientos_cerdo_fecha(f_i, f_f):  
    cerdos = Galpon.Movimientos_cerdo_fecha(f_i, f_f)
    print(cerdos)
    dicc = { 
         'cerdos': cerdos
    }
    return render_template('view/galpon/movimientos_cerdo.html', dicc = dicc)

#vista tipo de alimento
@index.route('/tipo_alimento')
def tipo_alimento():  
    return render_template('view/alimento/tipo_alimento.html')

#vista marca de alimento
@index.route('/marca_alimento')
def marca_alimento():  
    return render_template('view/alimento/marca_alimento.html')

#vista alimento de cerdos
@index.route('/alimento')
def alimento():  
    codigo = random.randint(0, 999999999)
    data = Alimento.Traer_tipo_alimento_select()
    marca = Alimento.Traer_marca_alimento_select()
    return render_template('view/alimento/alimento.html', codigo = codigo, data = data, marca = marca)

#vista alimento de cerdos
@index.route('/proveedor')
def proveedor():    
    return render_template('view/compras/proveedor.html')

#vista compras de alimentoa
@index.route('/compra_alimento')
def compra_alimento():   
    fecha = datetime.now()
    now = fecha.strftime("%Y-%m-%d")
    proveedor = Compras.Select_proveedor()
    alimentos = Compras.Table_alimentos()
    list_compras = Compras.Listar_compras_alimentos()
    data = {
        'fecha': now,
        'proveedor': proveedor,
        'alimentos': alimentos,
        'lista': list_compras
    }
    return render_template('view/compras/compra_alimento.html', data = data)

#vista tipo de alimentacion
@index.route('/tipo_alimentacion')
def tipo_alimentacion():    
    return render_template('view/alimento/tipo_alimentacion.html')

#vista alimentaion de cerdos
@index.route('/alimentacion_cerdos')
def alimentacion_cerdos():  
    fecha = datetime.now()
    now = fecha.strftime("%Y-%m-%d")
    tipo = Alimento.Traer_tipo_alimento_select() 
    tipo_a = Alimento.Traer_tipo_alimentacion_select() 
    galpon = Galpon.Listar_galpon_combo() 
    alimentacion = Alimento.Listar_alimentacion()
    cerdo = Galpon.Select_cerdos() 
    data = {
        'fecha': now,
        'tipo': tipo, 
        'tipo_a': tipo_a,
        'galpon': galpon,
        'alimentacion': alimentacion,
        'cerdo': cerdo, 
    }  
    return render_template('view/alimento/alimentacion_cerdos.html', data = data)

#vista movimientos de cerdos de galpones por fechas
@index.route('/alimentacion_cerdos_fecha/<string:f_i>/<string:f_f>')
def alimentacion_cerdos_fecha(f_i, f_f):  
    fecha = datetime.now()
    now = fecha.strftime("%Y-%m-%d")
    tipo = Alimento.Traer_tipo_alimento_select() 
    tipo_a = Alimento.Traer_tipo_alimentacion_select() 
    galpon = Galpon.Listar_galpon_combo() 
    alimentacion = Alimento.Listar_alimentacion_fecha(f_i,f_f)
    cerdo = Galpon.Select_cerdos() 
    data = {
        'fecha': now,
        'tipo': tipo, 
        'tipo_a': tipo_a,
        'galpon': galpon,
        'alimentacion': alimentacion,
        'cerdo': cerdo, 
    }  
    return render_template('view/alimento/alimentacion_cerdos.html', data = data)

#vista del pesaje de los cerdos
@index.route('/peso_cerdo')
def peso_cerdo():    
    fecha = datetime.now()
    now = fecha.strftime("%Y-%m-%d")
    cerdo = Galpon.Select_cerdos() 
    pesaje = Alimento.Listar_pesaje_cerdo()
    data = {
        'fecha': now,
        'cerdo': cerdo,  
        'pesaje': pesaje
    } 
    return render_template('view/alimento/peso_cerdo.html', data = data)

#vista movimientos de cerdos de galpones por fechas
@index.route('/peso_cerdos_fecha/<string:f_i>/<string:f_f>')
def peso_cerdos_fecha(f_i, f_f):  
    fecha = datetime.now()
    now = fecha.strftime("%Y-%m-%d")
    cerdo = Galpon.Select_cerdos() 
    pesaje = Alimento.Listar_pesaje_cerdo_fecha(f_i, f_f)
    data = {
        'fecha': now,
        'cerdo': cerdo,  
        'pesaje': pesaje
    } 
    return render_template('view/alimento/peso_cerdo.html', data = data)
