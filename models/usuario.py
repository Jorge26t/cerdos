from utils.db import mysql

class Usuario():
    # para e inicio de sesión
    def login(usuario, password):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT usuario_id, rol_id, estado  FROM usuario WHERE binary usuario = "{0}" AND binary passwordd = "{1}"'. format(
                usuario, password))
            data = query.fetchone()
            query.close()
            if not data:
                return 0
            else:
                return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para crear un nuevo rol
    def crear_rol(_rol):
        try:
            query = mysql.connection.cursor()
            query.execute(
                'SELECT * FROM rol WHERE binary rol = "{0}"'. format(_rol))
            data = query.fetchone()
            if not data:
                query.execute(
                    'INSERT INTO rol (rol) VALUES ("{0}")'.format(_rol))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo de listar rol
    def Listar_rol():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM rol')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id_rol"] = datos[0]
                dic["rol"] = datos[1]
                dic["estado"] = datos[2]
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado del rol
    def Estado_rol(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE rol SET estado = "{0}" WHERE rol_id = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el rol
    def Editar_rol(_rol, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM rol WHERE binary rol = "{0}" AND rol_id != "{1}"'. format(_rol, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE rol SET rol = "{0}" WHERE rol_id = "{1}"'.format(_rol, _id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo de listar rol
    def Listar_rol_combo():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT rol_id, rol FROM rol WHERE estado = 1')
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para crear un nuevo usuario
    def Craer_usuario(_nombres, _apellidos, _domicilio, _telefono, _tipo_rol, _usuario, _password, archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM usuario WHERE usuario = "{0}"'. format(_usuario))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO usuario (nombres, apellidos, usuario, passwordd, rol_id, domicilio, telefono, foto) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")'.format(_nombres, _apellidos, _usuario, _password, _tipo_rol, _domicilio, _telefono, archivo))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2 # usuario ya existe
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo de listar usuarios
    def Listar_usuarios():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        usuario.usuario_id,
                        usuario.nombres,
                        usuario.apellidos,
                        usuario.usuario,
                        usuario.passwordd,
                        usuario.rol_id,
                        usuario.domicilio,
                        usuario.telefono,
                        usuario.foto,
                        usuario.estado,
                        rol.rol 
                        FROM
                        usuario
                        INNER JOIN rol ON usuario.rol_id = rol.rol_id""")
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["nombres"] = datos[1]
                dic["apellidos"] = datos[2]
                dic["usuario"] = datos[3]
                dic["passwordd"] = datos[4]
                dic["rol_id"] = datos[5]
                dic["domicilio"] = datos[6]
                dic["telefono"] = datos[7]
                dic["foto"] = datos[8]
                dic["estado"] = datos[9]
                dic["rol"] = datos[10]
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado del usuario
    def Estado_usuario(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE usuario SET estado = "{0}" WHERE usuario_id = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para editar el usuario
    def Editar_usuario(_id, _nombres, _apellidos, _domicilio, _telefono, _tipo_rol, _usuario):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM usuario WHERE usuario = "{0}" AND usuario_id != "{1}"'. format(_usuario, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE usuario SET nombres = "{0}", apellidos = "{1}", usuario = "{2}", rol_id = "{3}", domicilio = "{4}", telefono = "{5}" WHERE usuario_id = "{6}"'.format(_nombres, _apellidos, _usuario, _tipo_rol, _domicilio, _telefono, _id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2 # usuario ya existe
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado del usuario
    def Editar_photo_user(_id, archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE usuario SET foto = "{0}" WHERE usuario_id = {1}'.format(archivo, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modeloa para traer los datos de la hacienda
    def Traer_hacienda():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM empresa WHERE id_hacienda = 1')
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para editar el usuario
    def Editar_empresa(_nombres, _ruc, _telefono, _direccion, _correo, _encargado, _descripcion):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE empresa SET nombre = "{0}", ruc = "{1}", telefono = "{2}", correo = "{3}", encargado = "{4}", descripcion = "{5}", direccion = "{6}" WHERE id_hacienda = 1'.format(_nombres, _ruc, _telefono, _correo, _encargado, _descripcion, _direccion))
            query.connection.commit()
            query.close()
            return 1  # editado correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para editar la imagen de empresa
    def Editar_photo_empresa(archivo):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE empresa SET foto = "{0}" WHERE id_hacienda = 1'.format(archivo))
            query.connection.commit()
            query.close()
            return 1  # editado correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para traer los datos del usuario
    def Datos_usuarios_logeo(_id, _id_rol):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
            usuario.usuario_id,
            usuario.nombres,
            usuario.apellidos,
            usuario.usuario,
            usuario.passwordd,
            usuario.rol_id,
            usuario.domicilio,
            usuario.telefono,
            usuario.foto,
            usuario.estado,
            rol.rol 
            FROM
            usuario
            INNER JOIN rol ON usuario.rol_id = rol.rol_id WHERE usuario.usuario_id = '{0}' AND usuario.rol_id = '{1}'""".format(_id, _id_rol))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para editar el usuario loegado
    def Editar_usuario_loegado(_id, _nombres, _apellidos, _domicilio, _telefono, _usuario):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM usuario WHERE usuario = "{0}" AND usuario_id != "{1}"'. format(_usuario, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE usuario SET nombres = "{0}", apellidos = "{1}", usuario = "{2}", domicilio = "{3}", telefono = "{4}" WHERE usuario_id = "{5}"'.format(_nombres, _apellidos, _usuario, _domicilio, _telefono, _id))
                query.connection.commit()
                query.close()
                return 1  # se inserto correcto
            else:
                query.close()
                return 2 # usuario ya existe
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para editar el password del usuario
    def Cambiar_password(_id, _password):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE usuario SET passwordd = "{0}" WHERE usuario_id = "{1}"'.format(_password, _id))
            query.connection.commit()
            query.close()
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0