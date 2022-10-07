from utils.db import mysql 

class Reportes():
     #modelo para traer los datos de la empresa
    def Traer_empresa():
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            empresa.nombre, 
                            empresa.telefono, 
                            empresa.correo, 
                            empresa.direccion
                        FROM
                            empresa""")
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    #modelo para traer el galpon de los cerdo
    def Listar_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            galpon.id_galpon,
                            galpon.numero, 
                            galpon.capacidad, 
                            COUNT(galpon_cerdo.id_cerdo) as cerdo,
                            tipo_galpon.tipo_galpon 
                            FROM
                            galpon
                            INNER JOIN galpon_cerdo ON galpon.id_galpon = galpon_cerdo.id_galpon
                            INNER JOIN tipo_galpon ON galpon.id_tipo = tipo_galpon.id_tipo  WHERE galpon.id_galpon = "{0}"
                            GROUP BY
                            galpon_cerdo.id_galpon""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer los cerdos del galpon
    def Cerdo_galpon(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            DATE(galpon_cerdo.fecha) as fecha,
                            cerdo.codigo,
                            cerdo.sexo,
                            raza.raza, 
                            cerdo.peso
                        FROM
                            galpon_cerdo
                            INNER JOIN cerdo ON galpon_cerdo.id_cerdo = cerdo.id_cerdo
                            INNER JOIN raza ON cerdo.raza = raza.id_raza WHERE galpon_cerdo.id_galpon = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    ######################### COMPRAS ALIMENTOS

    #modelo para listar la compra del alimento
    def Listar_compra_alimento(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_alimento.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon) AS proveedor,
                            proveedor.ruc,
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
                            INNER JOIN proveedor ON compra_alimento.proveedor_id = proveedor.id WHERE compra_alimento.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la compra
    def Detalle_compra_alimento(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            detalle_compra_alimento.compra_alimento_id,
                            alimento.codigo,
                            alimento.nombre,
                            detalle_compra_alimento.precio,
                            detalle_compra_alimento.cantidad,
                            detalle_compra_alimento.descuento,
                            detalle_compra_alimento.total,
                            detalle_compra_alimento.estado 
                        FROM
                            detalle_compra_alimento
                            INNER JOIN alimento ON detalle_compra_alimento.alimento_id = alimento.id 
                        WHERE
                            detalle_compra_alimento.compra_alimento_id = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 
    ######################### ALIMENTACION

    # modelo para listar la alimentación
    def Listar_alimentacion(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        alimentacion.id,
                        CONCAT_WS( " ", alimento.nombre, " - ", tipo_alimento.tipo_alimento ) AS alimento,
                        CONCAT_WS( " ", usuario.nombres ) AS usuario,
                        alimentacion.fecha,
                        alimentacion.cantidad,
                        alimentacion.observacion,
                        alimentacion.estado 
                        FROM
                        alimentacion
                        INNER JOIN alimento ON alimentacion.alimento_id = alimento.id
                        INNER JOIN tipo_alimento ON alimento.tipo_id = tipo_alimento.id
                        INNER JOIN usuario ON alimentacion.usuario_id = usuario.usuario_id WHERE alimentacion.id='{0}'""".format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    # modelo para listar los cerdos alimentados
    def Cerdos_alimentados(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                        CONCAT_WS( " ", cerdo.codigo, " - ", cerdo.nombre, " - ", raza.raza ) AS cerdo,
                        detalle_alimentacion.peso 
                       FROM
                        detalle_alimentacion
                        INNER JOIN cerdo ON detalle_alimentacion.id_cerdo = cerdo.id_cerdo
                        INNER JOIN raza ON cerdo.raza = raza.id_raza 
                        WHERE detalle_alimentacion.id_alimentacion = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0

    ######################### COMPRAS INSUMOS

    #modelo para listar la compra del insumo
    def Listar_compra_insumos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            compra_insumo.id,
                            CONCAT_WS( ' ', usuario.nombres, usuario.apellidos ) AS usuario,
                            CONCAT_WS( ' ', proveedor.razon) AS proveedor,
                            proveedor.ruc,
                            compra_insumo.fecha,
                            compra_insumo.numero_compra,
                            compra_insumo.documento,
                            compra_insumo.iva,
                            compra_insumo.subtotal,
                            compra_insumo.impuesto,
                            compra_insumo.total,
                            compra_insumo.estado 
                        FROM
                            compra_insumo
                            INNER JOIN usuario ON compra_insumo.usuario_id = usuario.usuario_id
                            INNER JOIN proveedor ON compra_insumo.proveedor_id = proveedor.id WHERE compra_insumo.id='{0}'""". format(id))
            data = query.fetchone()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
      
    #modelo para traer el detalle de la compra
    def Detalle_compra_insumos(id):
        try:
            query = mysql.connection.cursor()
            query.execute("""SELECT
                            detalle_compra_insumo.compra_insumo_id,
                            insumo.codigo,
                            insumo.nombre,
                            detalle_compra_insumo.precio,
                            detalle_compra_insumo.cantidad,
                            detalle_compra_insumo.descuento,
                            detalle_compra_insumo.total,
                            detalle_compra_insumo.estado 
                        FROM
                            detalle_compra_insumo
                            INNER JOIN insumo ON detalle_compra_insumo.insumo_id = insumo.id 
                        WHERE
                            detalle_compra_insumo.compra_insumo_id = '{0}'""".format(id))
            data = query.fetchall()
            query.close()
            return data
        except Exception as e:
            query.close()
            error = "Ocurrio un problema: " + str(e)
            return error
        return 0
 