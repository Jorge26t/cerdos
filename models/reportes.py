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
 
