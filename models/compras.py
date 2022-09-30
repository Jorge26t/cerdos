from utils.db import mysql
from datetime import datetime

class Compras():
    # modelo para registrar el proveedor
    def Registrar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor WHERE ruc = "{0}"'. format(_ruc))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO proveedor (razon,ruc,telefono,correo,descripcion,encargado,telefono_en,direccion) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")'.format(_razon_social,_ruc,_telefonoo,_correo,_descripcion,_encargdo,_telefonoo_en,_direccion))
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
    
    # modelo de listar el proveedor
    def Listado_proveedores():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor')
            data = query.fetchall()
            query.close()
            new_lista = []
            for datos in data:
                dic = {} 
                dic["id"] = datos[0]
                dic["razon"] = datos[1]
                dic["ruc"] = datos[2] 
                dic["telefono"] = datos[3]
                dic["correo"] = datos[4]
                dic["descripcion"] = datos[5] 
                dic["encargado"] = datos[6]
                dic["telefono_en"] = datos[7]
                dic["direccion"] = datos[8] 
                dic["estado"] = datos[9]       
                new_lista.append(dic)
            return {"data": new_lista}
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para estado del proveedor
    def Estado_proveedor(_id, _dato):
        try:
            query = mysql.connection.cursor()
            query.execute('UPDATE proveedor SET estado = "{0}" WHERE id = {1}'.format(_dato, _id))
            query.connection.commit()
            query.close()
            return 1  # se inserto correcto
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para editar el proveedor
    def Editar_proveedor(_razon_social, _ruc, _telefonoo, _correo, _descripcion, _encargdo, _telefonoo_en, _direccion, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor WHERE ruc="{0}" AND id != "{1}"'. format(_ruc, _id))
            data = query.fetchone()
            if not data:
                query.execute('UPDATE proveedor SET razon="{0}",ruc="{1}",telefono="{2}",correo="{3}",descripcion="{4}",encargado="{5}",telefono_en="{6}",direccion="{7}" WHERE id="{8}"'.format(_razon_social,_ruc,_telefonoo,_correo,_descripcion,_encargdo,_telefonoo_en,_direccion,_id))
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
    
    # modelo del select del proveedor
    def Select_proveedor():
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM proveedor WHERE estado = 1')
            data = query.fetchall()
            query.close()             
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar los alimentos para la compra
    def Table_alimentos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            alimento.id,
                            alimento.codigo,
                            alimento.nombre, 
                            alimento.cantidad,
                            alimento.precio,
                            alimento.peso, 
                            alimento.foto, 
                            marca_alimento.marca_alimento,
                            tipo_alimento.tipo_alimento 
                        FROM
                            alimento
                            INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                            INNER JOIN marca_alimento ON alimento.marca_id = marca_alimento.id WHERE alimento.estado = 1
                        ORDER BY
                            alimento.id DESC""")
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
   
    # controlador para registrar la compra
    def Registrar_compra_alimento(_id_pro, _fecha_c, _numero_compra, _tipo_comprobante, _iva, _subtotal, _impuesto_sub, _total_pagar, _id):
        try:
            query = mysql.connection.cursor()
            query.execute('SELECT * FROM compra_alimento WHERE numero_compra = "{0}"'. format(_numero_compra))
            data = query.fetchone()
            if not data:
                query.execute('INSERT INTO compra_alimento (usuario_id,proveedor_id,fecha,numero_compra,documento,iva,subtotal,impuesto,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(_id,_id_pro,_fecha_c,_numero_compra,_tipo_comprobante,_iva,_subtotal,_impuesto_sub,_total_pagar))
                query.connection.commit()
                # me devuelve el ultimo id insertado
                id = query.lastrowid
                query.close()
                return id  # se inserto correcto
            else:
                query.close()
                return 2
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # controlador para registra el detalle de compra del alimento
    def Registrar_detalle_compra_alimento(_id, ida, precio, cantidad, descuento, total):
        try:
            query = mysql.connection.cursor()         
            query.execute('INSERT INTO detalle_compra_alimento (compra_alimento_id,alimento_id,precio,cantidad,descuento,total) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(_id,ida,precio,cantidad,descuento,total))
            query.connection.commit()

            query.execute('UPDATE alimento SET cantidad = cantidad + "{0}" WHERE id = "{1}" '.format(cantidad,ida))
            query.connection.commit()

            query.close()
            return 1  # se inserto correcto

        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
    
    # modelo para listar las compras de alimentos
    def Listar_compras_alimentos():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_alimento.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon, ' - ', proveedor.ruc ) AS proveedor,
                            compra_alimento.fecha,
                            compra_alimento.numero_compra,
                            compra_alimento.documento,
                            compra_alimento.iva,
                            compra_alimento.subtotal,
                            compra_alimento.impuesto,
                            compra_alimento.total,
                            compra_alimento.estado 
                        FROM
                            compra_alimento
                            INNER JOIN usuario ON compra_alimento.usuario_id = usuario.usuario_id
                            INNER JOIN proveedor ON compra_alimento.proveedor_id = proveedor.id 
                        ORDER BY
                            compra_alimento.id DESC""")
            data = query.fetchall()
            query.close() 
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para anular la compra de alimentos
    def Anular_compra_alimentos(_id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT 
                            detalle_compra_alimento.alimento_id,
                            detalle_compra_alimento.cantidad 
                            FROM
                            detalle_compra_alimento
                            WHERE
                            detalle_compra_alimento.compra_alimento_id = '{0}'""".format(_id))
            data = query.fetchall()
            
            for dato in data: 
                query.execute('UPDATE alimento SET cantidad = cantidad - {0} WHERE id = "{1}"'.format(dato[1], str(dato[0])))
                query.connection.commit()

            query.execute('UPDATE compra_alimento SET estado = 0 WHERE id = {0}'.format(_id))
            query.connection.commit()

            query.execute('UPDATE detalle_compra_alimento SET estado = 0 WHERE id = "{0}"'.format(_id))
            query.connection.commit()
            query.close() 
            return 1
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
