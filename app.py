from flask import Flask
from flask_mysqldb import MySQL

from routers.index import index
from routers.usuario import usuario

app = Flask(__name__)
app.secret_key = 'my_secret_key'

# creo la conexion a la base de datos
# para instalar el modulo de MYSQL el comando es : pip instsall flask-mysqldb
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'elgamer1'
app.config['MYSQL_DB'] = 'tesis_cerdo'
# le paso la conexion al modulo
MySQL(app)

# esto llama la vista carpeta routes archivo
app.register_blueprint(index, url_prefix="/")
app.register_blueprint(usuario, url_prefix="/usuario")

#esta funcion ayuda controlar los errores cuanod no hay paginas
def pagna_error(error):
    return "paguina no enocntrada error 404", 404

