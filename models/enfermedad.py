from utils.db import mysql
from datetime import datetime

class Enfermedad():
    # modelo para crear el veterinrio
    def Registrar_veterinario(_nombre, _apellido, _numero_doc, _telefono, _direccion, _sucursal):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM veterinario WHERE documento = "{0}"'. format(_numero_doc))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO veterinario (nombre, apellido, documento, telefono, direccion, sucursal) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(_nombre,_apellido,_numero_doc,_telefono,_direccion,_sucursal))
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
    
    # modelo para listar el veterinario
    def Listar_veterinario():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM veterinario')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["nombre"] = datos[1]
                dic["apellido"] = datos[2]
                dic["documento"] = datos[3]
                dic["telefono"] = datos[4]
                dic["direccion"] = datos[5]
                dic["sucursal"] = datos[6] 
                dic["estado"] = datos[7]                
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado del veterinario
    def Estado_veterinario(_id,_dato):
        try:
            query = mysql.connection.cursor() 
            query.execute('UPDATE veterinario SET estado = "{0}" WHERE id = "{1}" '.format(_dato,_id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el veterinrio
    def Editar_veterinario(_nombre, _apellido, _numero_doc, _telefono, _direccion, _sucursal, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM veterinario WHERE documento="{0}" AND id!="{1}"'. format(_numero_doc, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE veterinario SET nombre="{0}", apellido="{1}", documento="{2}", telefono="{3}", direccion="{4}", sucursal="{5}" WHERE id="{6}"'.format(_nombre,_apellido,_numero_doc,_telefono,_direccion,_sucursal,_id))
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
    
    # modelo para crear la enfermedad
    def Registrar_tipo_enfermedad(_nombre, _descripcion):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM enfermedad WHERE nombre = "{0}"'. format(_nombre))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO enfermedad (nombre, descripcion) VALUES ("{0}","{1}")'.format(_nombre,_descripcion))
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
    
    # modelo para listar la enfermedad
    def Listar_enfermedad():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM enfermedad')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["nombre"] = datos[1]
                dic["descripcion"] = datos[2] 
                dic["estado"] = datos[3]                
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado de la enfermedad
    def Estado_enfermedad(_id,_dato):
        try:
            query = mysql.connection.cursor() 
            query.execute('UPDATE enfermedad SET estado = "{0}" WHERE id = "{1}" '.format(_dato,_id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar la enfermedad
    def Editar_tipo_enfermedad(_nombre, _descripcion, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM enfermedad WHERE nombre="{0}" AND id!="{1}"'. format(_nombre,_id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE enfermedad SET nombre="{0}", descripcion="{1}" WHERE id="{2}"'.format(_nombre,_descripcion,_id))
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
    
    # modelo para crear el tipo de tratamientos
    def Registrar_tipo_tratamiento(_nombre, _descripcion):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_tratamiento WHERE nombre = "{0}"'. format(_nombre))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO tipo_tratamiento (nombre, descripcion) VALUES ("{0}","{1}")'.format(_nombre,_descripcion))
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

    # modelo para listar el tipo de tratamiento
    def Listar_tipo_tratamiento():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_tratamiento')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {}
                dic["id"] = datos[0]
                dic["nombre"] = datos[1]
                dic["descripcion"] = datos[2] 
                dic["estado"] = datos[3]                
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado del tipo de tratamiento
    def Estado_tipo_tratamiento(_id,_dato):
        try:
            query = mysql.connection.cursor() 
            query.execute('UPDATE tipo_tratamiento SET estado = "{0}" WHERE id = "{1}" '.format(_dato,_id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el tipo de tratamientos
    def Editar_tipo_tratamiento(_nombre, _descripcion, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM tipo_tratamiento WHERE nombre = "{0}" AND id != "{1}"'. format(_nombre, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE tipo_tratamiento SET nombre="{0}", descripcion="{1}"WHERE id="{2}"'.format(_nombre,_descripcion,_id))
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
