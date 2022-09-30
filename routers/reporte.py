from flask import Blueprint, Response
from models.reportes import Reportes
import time
from os import getcwd
from fpdf import FPDF
from utils.referencias import *

# es un enrutador
# ojo cuando agas una redirecion usa index.luego la funcion
reporte = Blueprint('reporte', __name__)
PATH_FILE = getcwd() + "/static/uploads/cerdito.png"

def Empresa():
    empresa = Reportes.Traer_empresa()
    return empresa

#ver reporte de cerdos en galpon
@reporte.route('/reporte_galpo_cerdo/<int:id>')
def reporte_galpo_cerdo(id):
    fecha = time.strftime('%Y-%m-%d', time.localtime())
    empresa = Empresa()
    class PDF(FPDF):

        def header(self):

            self.image(PATH_FILE,  x=10, y=10, w=30, h=30)
            self.set_font('Arial', '', 15)

            tcol_set(self, 'blue')
            tfont_size(self, 35)
            tfont(self, 'B')
            self.cell(w=0, h=20, txt='     Reporte galpón cerdos', border=0, ln=1, align='C', fill=0)

            tfont_size(self, 10)
            tcol_set(self, 'black')
            tfont(self, 'I')
            self.cell(w=0, h=10, txt=fecha, border=0, ln=2, align='C', fill=0)

            tfont_size(pdf, 10)
            bcol_set(pdf, 'white')

            pdf.cell(w=65, h=5, txt='Empresa: ' + str(empresa[0]) , border=0,  fill=1)
            pdf.cell(w=55, h=5, txt='Telefono: ' + str(empresa[1]) , border=0,  fill=1) 
            pdf.multi_cell(w=0, h=5, txt='Dirección: ' + str(empresa[3]) , border=0, fill=1)
            
            self.ln(5)

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-20)

            # Arial italic 8
            self.set_font('Arial', 'I', 12)

            # Page number
            self.cell(w=0, h=10, txt='Pagina ' + str(self.page_no()) + '/{nb}', border=0, align='C', fill=0)
    
    #para traer el galpon de los cerdo
    data = Reportes.Listar_galpon(id)
    #para traer los cerdos del galpon
    lista_datos = Reportes.Cerdo_galpon(id)

    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.alias_nb_pages()

    pdf.add_page()

    # TEXTO
    pdf.set_font('Arial', '', 15)

    # 1er encabezado ----

    bcol_set(pdf, 'green')
    tfont_size(pdf, 15)
    tfont(pdf, 'B')
    pdf.multi_cell(w=0, h=10, txt='Galpón', border=0, align='C', fill=1)
    tfont(pdf, '')

    h_sep = 8
    pdf.ln(2)
    tfont_size(pdf, 12)

    # fila 1 --

    tcol_set(pdf, 'gray')
    pdf.cell(w=26, h=h_sep, txt='N° galpón: ', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=40, h=h_sep, txt=str(data[1]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=44, h=h_sep, txt='Tipo: ', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.multi_cell(w=0, h=h_sep, txt=str(data[4]), border=0, align='L', fill=0)

    # fila 2 --
    tcol_set(pdf, 'gray')
    pdf.cell(w=26, h=h_sep, txt='Capacidad:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=45, h=h_sep, txt=str(data[2]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=63, h=h_sep, txt='Cerdos en galpón:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.multi_cell(w=0, h=h_sep, txt=str(data[3]), border=0, align='L', fill=0)

    pdf.ln(2)
    # tabla ----

    bcol_set(pdf, 'green')
    tfont_size(pdf, 15)
    tfont(pdf, 'B')
    pdf.cell(w=0, h=10, txt='Cerdos dentro del galpón', border=0, ln=1, align='C', fill=1)
    tfont(pdf, '')

    tfont_size(pdf, 13)
    bcol_set(pdf, 'blue')

    pdf.cell(w=10, h=10, txt='#', border=0, align='C', fill=1)
    pdf.cell(w=30, h=10, txt='Fecha', border=0, align='C', fill=1)
    pdf.cell(w=50, h=10, txt='Código', border=0, align='C', fill=1)
    pdf.cell(w=30, h=10, txt='Sexo', border=0, align='C',fill=1)
    pdf.cell(w=30, h=10, txt='Raza', border=0, align='C',fill=1)
    pdf.multi_cell(w=0, h=10, txt='Peso kg', border=0, align='C',fill=1)

    tfont_size(pdf, 12)
    dcol_set(pdf, 'blue')
    tcol_set(pdf, 'gray')
    pdf.rect(x=10, y=60, w=190, h=53)
    c = 0
    
    for datos in lista_datos:
        
        c += 1
        if(c % 2 == 0):
            bcol_set(pdf, 'gray2')
        else:
            bcol_set(pdf, 'white')

        pdf.cell(w=10, h=10, txt=str(c), border='TBL', align='C', fill=1)
        pdf.cell(w=30, h=10, txt=str(datos[0]), border='TB', align='C', fill=1)
        pdf.cell(w=50, h=10, txt=str(datos[1]), border='TB', align='C', fill=1)
        pdf.cell(w=30, h=10, txt=str(datos[2]), border='TB', align='C', fill=1)
        pdf.cell(w=30, h=10, txt=str(datos[3]), border='TB', align='C', fill=1)        
        pdf.multi_cell(w=0, h=10, txt=str(datos[4]), border='TBR', align='C', fill=1)

    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition': 'inline;filename=Galpones_cerdos.pdf'})

#######################

#ver reporte de compras alimentos
@reporte.route('/compra_alimento/<int:id>')
def compra_alimento(id):
    fecha = time.strftime('%Y-%m-%d', time.localtime())
    empresa = Empresa()
    class PDF(FPDF):

        def header(self):

            self.image(PATH_FILE,  x=10, y=10, w=30, h=30)
            self.set_font('Arial', '', 15)

            tcol_set(self, 'blue')
            tfont_size(self, 35)
            tfont(self, 'B')
            self.cell(w=0, h=20, txt='     Compra de alimentos', border=0, ln=1, align='C', fill=0)

            tfont_size(self, 10)
            tcol_set(self, 'black')
            tfont(self, 'I')
            self.cell(w=0, h=10, txt=fecha, border=0, ln=2, align='C', fill=0)

            tfont_size(pdf, 10)
            bcol_set(pdf, 'white')

            pdf.cell(w=65, h=5, txt='Empresa: ' + str(empresa[0]) , border=0,  fill=1)
            pdf.cell(w=55, h=5, txt='Telefono: ' + str(empresa[1]) , border=0,  fill=1) 
            pdf.multi_cell(w=0, h=5, txt='Dirección: ' + str(empresa[3]) , border=0, fill=1)
            
            self.ln(5)

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-20)

            # Arial italic 8
            self.set_font('Arial', 'I', 12)

            # Page number
            self.cell(w=0, h=10, txt='Pagina ' + str(self.page_no()) + '/{nb}', border=0, align='C', fill=0)
    
    #para traer la compra del alimento
    data = Reportes.Listar_compra_alimento(id)
    #para traer el detalle de la compra
    lista_datos = Reportes.Detalle_compra_alimento(id)

    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.alias_nb_pages()

    pdf.add_page()

    # TEXTO
    pdf.set_font('Arial', '', 15)

    # 1er encabezado ----

    if data[11] != True :              
        tcol_set(pdf, 'black')
        bcol_set(pdf, 'red')
        tfont_size(pdf, 15)
        tfont(pdf, 'B')
        pdf.multi_cell(w=0, h=10, txt='LA COMPRA FUE ANULADA', border=0, align='C', fill=1)
        tfont(pdf, '')

    bcol_set(pdf, 'green')
    tfont_size(pdf, 15)
    tfont(pdf, 'B')
    pdf.multi_cell(w=0, h=10, txt='Compra', border=0, align='C', fill=1)
    tfont(pdf, '')

    h_sep = 8
    pdf.ln(2)
    tfont_size(pdf, 12)

    # fila 1 --

    tcol_set(pdf, 'gray')
    pdf.cell(w=26, h=h_sep, txt='Proveedor: ', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=40, h=h_sep, txt=str(data[2]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=44, h=h_sep, txt='Rúc: ', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.multi_cell(w=0, h=h_sep, txt=str(data[3]), border=0, align='L', fill=0)

    # fila 2 --
    tcol_set(pdf, 'gray')
    pdf.cell(w=17, h=h_sep, txt='Fecha:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=25, h=h_sep, txt=str(data[4]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=30, h=h_sep, txt='N° compra:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=20, h=h_sep, txt=str(data[5]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=45, h=h_sep, txt='Documento:', border=0, align='R', fill=0)

    if(data[6] == 'Factura'):
        tipo = "Factura"
    else:
        tipo = "Nota compra"

    tcol_set(pdf, 'black')
    pdf.cell(w=20, h=h_sep, txt=str(tipo), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=15, h=h_sep, txt='Iva:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.multi_cell(w=0, h=h_sep, txt=str(data[7]) + "%", border=0, align='L', fill=0)

    pdf.ln(2)
    # tabla ----

    bcol_set(pdf, 'green')
    tfont_size(pdf, 15)
    tfont(pdf, 'B')
    pdf.cell(w=0, h=10, txt='Alimentos comprados', border=0, ln=1, align='C', fill=1)
    tfont(pdf, '')

    tfont_size(pdf, 13)
    bcol_set(pdf, 'blue')

    pdf.cell(w=7, h=10, txt='#', border=0, align='C', fill=1) 
    pdf.cell(w=75, h=10, txt='Alimento', border=0, align='C', fill=1)
    pdf.cell(w=25, h=10, txt='Precio', border=0, align='C',fill=1)
    pdf.cell(w=25, h=10, txt='Cantidad', border=0, align='C',fill=1)
    pdf.cell(w=25, h=10, txt='Descuento', border=0, align='C',fill=1) 
    pdf.multi_cell(w=0, h=10, txt='Total', border=0, align='C',fill=1)

    tfont_size(pdf, 12)
    dcol_set(pdf, 'blue')
    tcol_set(pdf, 'gray')
    pdf.rect(x=10, y=60, w=190, h=53)
    c = 0
    
    for datos in lista_datos:
        
        c += 1
        if(c % 2 == 0):
            bcol_set(pdf, 'gray2')
        else:
            bcol_set(pdf, 'white')

        pdf.cell(w=7, h=10, txt=str(c), border='TBL', align='C', fill=1) 
        pdf.cell(w=75, h=10, txt=str(datos[2]), border='TB', align='C', fill=1)
        pdf.cell(w=25, h=10, txt="$ " + str(datos[3]), border='TB', align='C', fill=1)
        pdf.cell(w=25, h=10, txt=str(datos[4]), border='TB', align='C', fill=1)   
        pdf.cell(w=25, h=10, txt="$ " + str(datos[5]), border='TB', align='C', fill=1)        
        pdf.multi_cell(w=0, h=10, txt="$ " + str(datos[6]), border='TBR', align='C', fill=1)

    tcol_set(pdf, 'black') 
    pdf.cell(w=7, h=10, txt="", border='TBL', align='C', fill=1) 
    pdf.cell(w=75, h=10, txt="", border='TB', align='C', fill=1)
    pdf.cell(w=25, h=10, txt="", border='TB', align='C', fill=1)
    pdf.cell(w=25, h=10, txt="", border='TB', align='C', fill=1)   
    pdf.cell(w=25, h=10, txt="SubTotal: ", border='TB', align='C', fill=1)        
    pdf.multi_cell(w=0, h=10, txt="$ " + str(data[8]), border='TBR', align='C', fill=1)

    pdf.cell(w=7, h=10, txt="", border='TBL', align='C', fill=1) 
    pdf.cell(w=75, h=10, txt="", border='TB', align='C', fill=1)
    pdf.cell(w=25, h=10, txt="", border='TB', align='C', fill=1)
    pdf.cell(w=25, h=10, txt="", border='TB', align='C', fill=1)   
    pdf.cell(w=25, h=10, txt="Impuesto: ", border='TB', align='C', fill=1)        
    pdf.multi_cell(w=0, h=10, txt="$ " + str(data[9]), border='TBR', align='C', fill=1)

    pdf.cell(w=7, h=10, txt="", border='TBL', align='C', fill=1) 
    pdf.cell(w=75, h=10, txt="", border='TB', align='C', fill=1)
    pdf.cell(w=25, h=10, txt="", border='TB', align='C', fill=1)
    pdf.cell(w=25, h=10, txt="", border='TB', align='C', fill=1)   
    pdf.cell(w=25, h=10, txt="Total: ", border='TB', align='C', fill=1)        
    pdf.multi_cell(w=0, h=10, txt="$ " + str(data[10]), border='TBR', align='C', fill=1)

    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition': 'inline;filename=Galpones_cerdos.pdf'})

#######################

#ver reporte de compras alimentos
@reporte.route('/reporte_alimentacion/<int:id>')
def reporte_alimentacion(id):
    fecha = time.strftime('%Y-%m-%d', time.localtime())
    empresa = Empresa()
    class PDF(FPDF):

        def header(self):

            self.image(PATH_FILE,  x=10, y=10, w=30, h=30)
            self.set_font('Arial', '', 15)

            tcol_set(self, 'blue')
            tfont_size(self, 35)
            tfont(self, 'B')
            self.cell(w=0, h=20, txt='     Alimentación de cerdos', border=0, ln=1, align='C', fill=0)

            tfont_size(self, 10)
            tcol_set(self, 'black')
            tfont(self, 'I')
            self.cell(w=0, h=10, txt=fecha, border=0, ln=2, align='C', fill=0)

            tfont_size(pdf, 10)
            bcol_set(pdf, 'white')

            pdf.cell(w=65, h=5, txt='Empresa: ' + str(empresa[0]) , border=0,  fill=1)
            pdf.cell(w=55, h=5, txt='Telefono: ' + str(empresa[1]) , border=0,  fill=1) 
            pdf.multi_cell(w=0, h=5, txt='Dirección: ' + str(empresa[3]) , border=0, fill=1)
            
            self.ln(5)

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-20)

            # Arial italic 8
            self.set_font('Arial', 'I', 12)

            # Page number
            self.cell(w=0, h=10, txt='Pagina ' + str(self.page_no()) + '/{nb}', border=0, align='C', fill=0)
    
    #para traer la compra del alimento
    data = Reportes.Listar_alimentacion(id)
    #para traer el detalle de la compra
    lista_datos = Reportes.Cerdos_alimentados(id)

    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.alias_nb_pages()

    pdf.add_page()

    # TEXTO
    pdf.set_font('Arial', '', 15)

    # 1er encabezado ----

    bcol_set(pdf, 'green')
    tfont_size(pdf, 15)
    tfont(pdf, 'B')
    pdf.multi_cell(w=0, h=10, txt='Alimento', border=0, align='C', fill=1)
    tfont(pdf, '')

    h_sep = 8
    pdf.ln(2)
    tfont_size(pdf, 12)

    # fila 1 --

    tcol_set(pdf, 'gray')
    pdf.cell(w=22, h=h_sep, txt='Alimento: ', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=40, h=h_sep, txt=str(data[1]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=60, h=h_sep, txt='Usuario: ', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.multi_cell(w=0, h=h_sep, txt=str(data[2]), border=0, align='L', fill=0)

    # fila 2 --
    tcol_set(pdf, 'gray')
    pdf.cell(w=17, h=h_sep, txt='Fecha:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=25, h=h_sep, txt=str(data[3]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=60, h=h_sep, txt='Cantidad sacos:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.cell(w=20, h=h_sep, txt=str(data[4]), border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=45, h=h_sep, txt='', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.multi_cell(w=0, h=h_sep, txt="", border=0, align='L', fill=0)

    tcol_set(pdf, 'gray')
    pdf.cell(w=28, h=h_sep, txt='Observación:', border=0, align='R', fill=0)

    tcol_set(pdf, 'black')
    pdf.multi_cell(w=0, h=h_sep, txt=str(data[5]), border=0, align='L', fill=0)

    pdf.ln(2)
    # tabla ----

    bcol_set(pdf, 'green')
    tfont_size(pdf, 15)
    tfont(pdf, 'B')
    pdf.cell(w=0, h=10, txt='Cerdos alimentados', border=0, ln=1, align='C', fill=1)
    tfont(pdf, '')

    tfont_size(pdf, 13)
    bcol_set(pdf, 'blue')

    pdf.cell(w=7, h=10, txt='#', border=0, align='C', fill=1) 
    pdf.cell(w=120, h=10, txt='Cerdos', border=0, align='C', fill=1) 
    pdf.multi_cell(w=0, h=10, txt='Peso (Kg)', border=0, align='C',fill=1)

    tfont_size(pdf, 12)
    dcol_set(pdf, 'blue')
    tcol_set(pdf, 'gray')
    pdf.rect(x=10, y=60, w=190, h=53)
    c = 0
    
    for datos in lista_datos:
        
        c += 1
        if(c % 2 == 0):
            bcol_set(pdf, 'gray2')
        else:
            bcol_set(pdf, 'white')

        pdf.cell(w=7, h=10, txt=str(c), border='TBL', align='C', fill=1) 
        pdf.cell(w=120, h=10, txt=str(datos[0]), border='TB', align='C', fill=1)       
        pdf.multi_cell(w=0, h=10, txt=str(datos[1]) + " Kg", border='TBR', align='C', fill=1)

    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition': 'inline;filename=Galpones_cerdos.pdf'})




 
    