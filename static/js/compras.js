var tabla_proveedor;

function registro_proveedor() { 
    var razon_social = $("#razon_social").val();
    var ruc = $("#ruc").val();
    var telefonoo = $("#telefonoo").val();
    var correo = $("#correo").val();
    var direccion = $("#direccion").val();
    var descripcion = $("#descripcion").val();
    var encargdo = $("#encargdo").val();
    var telefonoo_en = $("#telefonoo_en").val();
  
    if (
      razon_social.length == 0 ||
      razon_social.trim() == "" ||
      ruc.length == 0 ||
      ruc.trim() == "" ||
      telefonoo.length == 0 ||
      telefonoo.trim() == "" ||
      correo.length == 0 ||
      correo.trim() == "" ||
      direccion.length == 0 ||
      direccion.trim() == "" ||
      descripcion.length == 0 ||
      descripcion.trim() == "" ||
      encargdo.length == 0 ||
      encargdo.trim() == "" ||
      telefonoo_en.length == 0 ||
      telefonoo_en.trim() == ""
    ) {
      validar_registro_proveedor(
        razon_social,
        ruc,
        telefonoo,
        correo,
        direccion,
        descripcion,
        encargdo,
        telefonoo_en
      );
  
      return swal.fire(
        "Campo vacios",
        "Los campos no deben quedar vacios, complete los datos",
        "warning"
      );
    } else { 
        $("#razon_social_oblig").html(""); 
        $("#ruc_obligg").html(""); 
        $("#telefonoo_obligg").html(""); 
        $("#correo_obligg").html(""); 
        $("#direccion_obligg").html(""); 
        $("#descripcion_obligg").html(""); 
        $("#encargdo_oblig").html(""); 
        $("#telefonoo_en__obligg").html("");
    }

    if(!valid_email){
        return swal.fire(
            "Correo incorrecto",
            "El correo ingresado es incorrecto",
            "warning"
          );
    }
  
    var formdata = new FormData(); 
    formdata.append("razon_social", razon_social);
    formdata.append("ruc", ruc);
    formdata.append("telefonoo", telefonoo);
    formdata.append("correo", correo);
    formdata.append("direccion", direccion);
    formdata.append("descripcion", descripcion);
    formdata.append("encargdo", encargdo);
    formdata.append("telefonoo_en", telefonoo_en); 
  
    $.ajax({
      url: "/compras/registrar_proveedor",
      type: "POST",
      //aqui envio toda la formdata
      data: formdata,
      contentType: false,
      processData: false,
      success: function (resp) {
        if (resp > 0) {
          if (resp == 1) {
            $(".card-success").LoadingOverlay("hide");               
            cargar_contenido('contenido_principal','/proveedor');
            return Swal.fire(
              "Proveedor registrado con exito",
              "El proveedor se registro con exito",
              "success"
            );
          } else if (resp == 2) {
            $(".card-success").LoadingOverlay("hide");
            return Swal.fire(
              "Rúc ya existe",
              "El rúc '" + ruc + "', ya existe en el sistema",
              "warning"
            );
          }
        } else {
          $(".card-success").LoadingOverlay("hide");
          return Swal.fire(
            "Error",
            "No se pudo registrar el proveedor, falla en la matrix",
            "error"
          );
        }
      },
      beforeSend: function () {
        $(".card-success").LoadingOverlay("show", {
          text: "Cargando...",
        });
      },
    });
    return false;
}
  
function validar_registro_proveedor(
    razon_social,
    ruc,
    telefonoo,
    correo,
    direccion,
    descripcion,
    encargdo,
    telefonoo_en
  ) {
    if (razon_social.length == 0 || razon_social.trim() == "") {
      $("#razon_social_oblig").html("Ingrese razón social");
    } else {
      $("#razon_social_oblig").html("");
    }
  
    if (ruc.length == 0 || ruc.trim() == "") {
      $("#ruc_obligg").html("Ingrese el ruc");
    } else {
      $("#ruc_obligg").html("");
    }
  
    if (telefonoo.length == 0  || telefonoo.trim() == "") {
      $("#telefonoo_obligg").html("Ingrese el telefono");
    } else {
      $("#telefonoo_obligg").html("");
    }
  
    if (correo.length == 0 || correo.trim() == "") {
      $("#correo_obligg").html("Ingrese el correo");
    } else {
      $("#correo_obligg").html("");
    }
  
    if (direccion.length == 0 || direccion.trim() == "") {
      $("#direccion_obligg").html("Ingrese la dirección");
    } else {
      $("#direccion_obligg").html("");
    }
  
    if (descripcion.length == 0 || descripcion.trim() == "") {
      $("#descripcion_obligg").html("Ingrese la descripción");
    } else {
      $("#descripcion_obligg").html("");
    }
  
    if (encargdo.length == 0 || encargdo.trim() == "") {
      $("#encargdo_oblig").html("Ingrese el encargdo");
    } else {
      $("#encargdo_oblig").html("");
    }
  
    if (telefonoo_en.length == 0 || telefonoo_en.trim() == "") {
      $("#telefonoo_en__obligg").html("Ingrese el telefono del encargado");
    } else {
      $("#telefonoo_en__obligg").html("");
    }
}

function listado_proveedores() {
    tabla_proveedor = $("#tabla_proveedore").DataTable({
      ordering: true,
      paging: true,
      aProcessing: true,
      aServerSide: true,
      searching: { regex: true },
      lengthMenu: [
        [10, 25, 50, 100, -1],
        [10, 25, 50, 100, "All"],
      ],
      pageLength: 10,
      destroy: true,
      async: false,
      processing: true,
  
      ajax: {
        url: "/compras/listado_proveedores",
        type: "GET",
      },
      //hay que poner la misma cantidad de columnas y tambien en el html
      columns: [
        { defaultContent: "" },
        {
          data: "estado",
          render: function (data, type, row) {
            if (data == 1) {
              return `<button style='font-size:10px;' type='button' class='inactivar btn btn-outline-danger' title='Inactivar el cerdo'><i class='fa fa-times' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cerdo'><i class='fa fa-edit' style='font-size: 15px;'></i></button>`;
            } else {
              return `<button style='font-size:10px;' type='button' class='activar btn btn-outline-success' title='Activar el cerdo'><i class='fa fa-check' style='font-size: 15px;'></i></button> - <button style='font-size:10px;' type='button' class='editar btn btn-outline-primary' title='Editar el cerdo'><i class='fa fa-edit' style='font-size: 15px;'></i></button>`;
            }
          },
        },
        { data: "razon" },
        { data: "ruc" },
        { data: "telefono" },
        { data: "correo" },     
        { data: "direccion" },
        { data: "encargado" },
        { data: "telefono_en" },
        { data: "descripcion" },
        {
          data: "estado",
          render: function (data, type, row) {
            if (data == 1) {
              return "<span class='badge badge-success'>ACTIVO</span>";
            } else {
              return "<span class='badge badge-danger'>INACTIVO</span>";
            }
          },
        },
      ],
      language: {
        rows: "%d fila seleccionada",
        processing: "Tratamiento en curso...",
        search: "Buscar&nbsp;:",
        lengthMenu: "Agrupar en _MENU_ items",
        info: "Mostrando los item (_START_ al _END_) de un total _TOTAL_ items",
        infoEmpty: "No existe datos.",
        infoFiltered: "(filtrado de _MAX_ elementos en total)",
        infoPostFix: "",
        loadingRecords: "Cargando...",
        zeroRecords: "No se encontro resultados en tu busqueda",
        emptyTable: "No hay datos disponibles en la tabla",
        paginate: {
          first: "Primero",
          previous: "Anterior",
          next: "Siguiente",
          last: "Ultimo",
        },
        select: {
          rows: "%d fila seleccionada",
        },
        aria: {
          sortAscending: ": active para ordenar la columa en orden ascendente",
          sortDescending: ": active para ordenar la columna en orden descendente",
        },
      },
      select: true,
      responsive: "true",
      dom: "Bfrtilp",
      buttons: [
        {
          extend: "excelHtml5",
          text: "Excel",
          titleAttr: "Exportar a Excel",
          className: "btn btn-success greenlover",
        },
        {
          extend: "pdfHtml5",
          text: "PDF",
          titleAttr: "Exportar a PDF",
          className: "btn btn-danger redfule",
        },
        {
          extend: "print",
          text: "Imprimir",
          titleAttr: "Imprimir",
          className: "btn btn-primary azuldete",
        },
      ],
      order: [[0, "ASC"]],
    });
  
    //esto es para crearn un contador para la tabla este contador es automatico
    tabla_proveedor.on("draw.dt", function () {
      var pageinfo = $("#tabla_proveedore").DataTable().page.info();
      tabla_proveedor
        .column(0, { page: "current" })
        .nodes()
        .each(function (cell, i) {
          cell.innerHTML = i + 1 + pageinfo.start;
        });
    });
}

$("#tabla_proveedore").on("click", ".inactivar", function () {
    //esto esta extrayendo los datos de la tabla el (data)
    var data = tabla_proveedor.row($(this).parents("tr")).data(); //a que fila deteta que doy click
    //esta condicion es importante para el responsibe porque salda un error si no lo pongo
    if (tabla_proveedor.row(this).child.isShown()) {
      //esto es cuando esta en tamaño responsibo
      var data = tabla_proveedor.row(this).data();
    }
    var dato = 0;
    var id = data.id;
  
    Swal.fire({
      title: "Cambiar estado?",
      text: "El estado del proveedor se cambiara!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Si, cambiar!",
    }).then((result) => {
      if (result.isConfirmed) {
        cambiar_estado_proveedor(id, dato);
      }
    });
});
  
$("#tabla_proveedore").on("click", ".activar", function () {
    //esto esta extrayendo los datos de la tabla el (data)
    var data = tabla_proveedor.row($(this).parents("tr")).data(); //a que fila deteta que doy click
    //esta condicion es importante para el responsibe porque salda un error si no lo pongo
    if (tabla_proveedor.row(this).child.isShown()) {
      //esto es cuando esta en tamaño responsibo
      var data = tabla_proveedor.row(this).data();
    }
    var dato = 1;
    var id = data.id;
  
    Swal.fire({
      title: "Cambiar estado?",
      text: "El estado del proveedor se cambiara!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Si, cambiar!",
    }).then((result) => {
      if (result.isConfirmed) {
        cambiar_estado_proveedor(id, dato);
      }
    });
});
  
function cambiar_estado_proveedor(id, dato) {
    var res = "";
    if (dato == 1) {
      res = "activo";
    } else {
      res = "inactivo";
    }
  
    $.ajax({
      url: "/compras/estado_proveedor",
      type: "POST",
      data: { id: id, dato: dato },
    }).done(function (response) {
      if (response > 0) {
        if (response == 1) {
          tabla_proveedor.ajax.reload();
          return Swal.fire(
            "Estado proveedor",
            "EL estado se " + res + " con extio",
            "success"
          );
        }
      } else {
        return Swal.fire(
          "Estado rol",
          "No se pudo cambiar el estado, error en la matrix",
          "error"
        );
      }
    });
}
  
$("#tabla_proveedore").on("click", ".editar", function () {
    //esto esta extrayendo los datos de la tabla el (data)
    var data = tabla_proveedor.row($(this).parents("tr")).data(); //a que fila deteta que doy click
    //esta condicion es importante para el responsibe porque salda un error si no lo pongo
    if (tabla_proveedor.row(this).child.isShown()) {
      //esto es cuando esta en tamaño responsibo
      var data = tabla_proveedor.row(this).data();
    }

    $("#id_proveedor").val(data.id);
    $("#razon_social_edit").val(data.razon);
    $("#ruc_edit").val(data.ruc);
    $("#telefonoo_edit").val(data.telefono);
    $("#correo_edit").val(data.correo);
    $("#direccion_edit").val(data.direccion);
    $("#descripcion_edit").val(data.descripcion);
    $("#encargdo_edit").val(data.encargado);
    $("#telefonoo_en_edit").val(data.telefono_en);

    $("#razon_social_oblig_edit").html(""); 
    $("#ruc_oblig_edit").html(""); 
    $("#telefonoo_oblig_edit").html(""); 
    $("#correo_oblig_edit").html(""); 
    $("#direccion_oblig_edit").html(""); 
    $("#descripcion_oblig_edit").html(""); 
    $("#encargdo_oblig_edit").html(""); 
    $("#telefonoo_en_oblig_edit").html("");
  
    $("#modal_editar_proveedor").modal({ backdrop: "static", keyboard: false });
    $("#modal_editar_proveedor").modal("show");
});

function editar_proveedor() { 
  var id = $("#id_proveedor").val();
  var razon_social = $("#razon_social_edit").val();
  var ruc = $("#ruc_edit").val();
  var telefonoo = $("#telefonoo_edit").val();
  var correo = $("#correo_edit").val();
  var direccion = $("#direccion_edit").val();
  var descripcion = $("#descripcion_edit").val();
  var encargdo = $("#encargdo_edit").val();
  var telefonoo_en = $("#telefonoo_en_edit").val();

  if (
    razon_social.length == 0 ||
    razon_social.trim() == "" ||
    ruc.length == 0 ||
    ruc.trim() == "" ||
    telefonoo.length == 0 ||
    telefonoo.trim() == "" ||
    correo.length == 0 ||
    correo.trim() == "" ||
    direccion.length == 0 ||
    direccion.trim() == "" ||
    descripcion.length == 0 ||
    descripcion.trim() == "" ||
    encargdo.length == 0 ||
    encargdo.trim() == "" ||
    telefonoo_en.length == 0 ||
    telefonoo_en.trim() == ""
  ) {
    validar_editar_proveedor(
      razon_social,
      ruc,
      telefonoo,
      correo,
      direccion,
      descripcion,
      encargdo,
      telefonoo_en
    );

    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else { 
      $("#razon_social_oblig_edit").html(""); 
      $("#ruc_oblig_edit").html(""); 
      $("#telefonoo_oblig_edit").html(""); 
      $("#correo_oblig_edit").html(""); 
      $("#direccion_oblig_edit").html(""); 
      $("#descripcion_oblig_edit").html(""); 
      $("#encargdo_oblig_edit").html(""); 
      $("#telefonoo_en_oblig_edit").html("");
  }

  var formdata = new FormData(); 
  formdata.append("id", id);
  formdata.append("razon_social", razon_social);
  formdata.append("ruc", ruc);
  formdata.append("telefonoo", telefonoo);
  formdata.append("correo", correo);
  formdata.append("direccion", direccion);
  formdata.append("descripcion", descripcion);
  formdata.append("encargdo", encargdo);
  formdata.append("telefonoo_en", telefonoo_en); 

  $.ajax({
    url: "/compras/editar_proveedor",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $(".bg-primary").LoadingOverlay("hide");               
          $("#modal_editar_proveedor").modal("hide");
          tabla_proveedor.ajax.reload();
          return Swal.fire(
            "Proveedor editado con exito",
            "El proveedor se edito con exito",
            "success"
          );
        } else if (resp == 2) {
          $(".bg-primary").LoadingOverlay("hide");
          return Swal.fire(
            "Rúc ya existe",
            "El rúc '" + ruc + "', ya existe en el sistema",
            "warning"
          );
        }
      } else {
        $(".bg-primary").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo editar el proveedor, falla en la matrix",
          "error"
        );
      }
    },
    beforeSend: function () {
      $(".bg-primary").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

function validar_editar_proveedor(
  razon_social,
  ruc,
  telefonoo,
  correo,
  direccion,
  descripcion,
  encargdo,
  telefonoo_en
) {
  if (razon_social.length == 0 || razon_social.trim() == "") {
    $("#razon_social_oblig_edit").html("Ingrese razón social");
  } else {
    $("#razon_social_oblig_edit").html("");
  }

  if (ruc.length == 0 || ruc.trim() == "") {
    $("#ruc_oblig_edit").html("Ingrese el ruc");
  } else {
    $("#ruc_oblig_edit").html("");
  }

  if (telefonoo.length == 0  || telefonoo.trim() == "") {
    $("#telefonoo_oblig_edit").html("Ingrese el telefono");
  } else {
    $("#telefonoo_oblig_edit").html("");
  }

  if (correo.length == 0 || correo.trim() == "") {
    $("#correo_oblig_edit").html("Ingrese el correo");
  } else {
    $("#correo_oblig_edit").html("");
  }

  if (direccion.length == 0 || direccion.trim() == "") {
    $("#direccion_oblig_edit").html("Ingrese la dirección");
  } else {
    $("#direccion_oblig_edit").html("");
  }

  if (descripcion.length == 0 || descripcion.trim() == "") {
    $("#descripcion_oblig_edit").html("Ingrese la descripción");
  } else {
    $("#descripcion_oblig_edit").html("");
  }

  if (encargdo.length == 0 || encargdo.trim() == "") {
    $("#encargdo_oblig_edit").html("Ingrese el encargdo");
  } else {
    $("#encargdo_oblig_edit").html("");
  }

  if (telefonoo_en.length == 0 || telefonoo_en.trim() == "") {
    $("#telefonoo_en_oblig_edit").html("Ingrese el telefono del encargado");
  } else {
    $("#telefonoo_en_oblig_edit").html("");
  }
}

////////////////////////
/////////// compras de alimentos para cerdos
function registra_compra_alimento(){
  Swal.fire({
    title: 'Guardar compra de alimento?',
    text: "La compra se guardará en el sistema!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, guardar!'
  }).then((result) => {
    if (result.isConfirmed) {
      guardar_compra_alimento();
    }
  })
}

function guardar_compra_alimento(){
  var proveedor = $("#proveedor").val(); 
  var fecha_c = $("#fecha_c").val(); 
  var numero_compra = $("#numero_compra").val(); 
  var tipo_comprobante = $("#tipo_comprobante").val(); 
  var iva = $("#iva").val(); 

  var subtotal = $("#subtotal").val(); 
  var impuesto_sub = $("#impuesto_sub").val(); 
  var total_pagar = $("#total_pagar").val(); 
  var count = 0;

  if(proveedor == "0" || 
  numero_compra.length == 0 || 
  numero_compra.trim() == "" ||
  iva.length == 0 || 
  iva.trim() == ""){
    validar_registro_compra(proveedor,numero_compra,iva);
    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  }else{ 
      $("#proveedor_obligg").html(""); 
      $("#numero_c_obligg").html(""); 
      $("#ivaa_obligg").html("");
  }

  $("#tabla_compra_alimento tbody#tbody_tabla_compra_alimento tr").each(function () {
      count++;
    }
  );

  if(count == 0){ 
    $("#unir_no_hay").html('<span class="badge badge-danger"><b>.:No hay alimentos en el detalle de compra:.</b></span>');
    return swal.fire(
      "Detalle vacío",
      "No hay alimentos en el detalle de compra",
      "warning"
    );
  }else{
    $("#unir_no_hay").html("");
  }

  var formdata = new FormData();
  formdata.append("proveedor", proveedor);
  formdata.append("fecha_c", fecha_c);
  formdata.append("numero_compra", numero_compra);
  formdata.append("tipo_comprobante", tipo_comprobante);
  formdata.append("iva", iva);
  formdata.append("subtotal", subtotal);
  formdata.append("impuesto_sub", impuesto_sub);
  formdata.append("total_pagar", total_pagar); 

  $.ajax({
    url: "/compras/registrar_compra_alimento",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp != 2) {

          guardar_detalle_compra_alimento(parseInt(resp));

        } else {
          $(".card-success").LoadingOverlay("hide");
          return Swal.fire(
            "Número de compra ya existe",
            "El número de compra: '" + numero_compra + "', ya existe en el sistema",
            "warning"
          );

        } 

      } else {

        $(".card-success").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo crear la comppra, falla en la matrix",
          "error"
        );
      }
    },

    beforeSend: function () {
      $(".card-success").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

function guardar_detalle_compra_alimento(id){
  var count = 0;
  var arrego_alimento = new Array();
  var arreglo_precio = new Array();
  var arreglo_cantidad = new Array();
  var arreglo_descuento = new Array();
  var arreglo_subtotal = new Array();

  $("#tabla_compra_alimento tbody#tbody_tabla_compra_alimento tr").each(
    function () {
      arrego_alimento.push($(this).find("td").eq(0).text());
      arreglo_precio.push($(this).find("td").eq(3).text());
      arreglo_cantidad.push($(this).find("#cantida_a").val());
      arreglo_descuento.push($(this).find("#descuento_a").val());
      arreglo_subtotal.push($(this).find("td").eq(6).text());
      count++;
    }
  );

  //aqui combierto el arreglo a un string
  var ida = arrego_alimento.toString();
  var precio = arreglo_precio.toString();
  var cantidad = arreglo_cantidad.toString();
  var descuento = arreglo_descuento.toString();
  var total = arreglo_subtotal.toString();

  if (count == 0) {
    return false;
  }

  $.ajax({
    url: "/compras/registrar_detalle_compra_alimento",
    type: "POST",
    data: { 
      id: id,
      ida: ida,
      precio: precio,
      cantidad: cantidad,
      descuento: descuento,
      total: total,
    },
  }).done(function (resp) {
    if (resp > 0) {
      if (resp == 1) {
        Swal.fire({
          title: "Campra realizada con exito",
          text: "Desea imprimir la compra??",
          icon: "warning",
          showCancelButton: true,
          showConfirmButton: true,
          allowOutsideClick: false,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Si, Imprimir!!",
        }).then((result) => {
          if (result.value) {
            window.open("/reporte/compra_alimento/" + parseInt(id) + "#zoom=100%", "Reporte de compra","scrollbards=No");
            cargar_contenido('contenido_principal','/compra_alimento');
          }
        });
        cargar_contenido('contenido_principal','/compra_alimento');
      }
    } else {

      return Swal.fire(
        "Error",
        "No se pudo crear el detalle de comppra, falla en la matrix",
        "error"
      );

    }
  });
}

function validar_registro_compra(proveedor,numero_compra,iva) {
  if (proveedor == "0") {
    $("#proveedor_obligg").html("Seleccione el proveedor");
  } else {
    $("#proveedor_obligg").html("");
  }

  if (numero_compra.length == 0 || numero_compra.trim() == "") {
    $("#numero_c_obligg").html("Ingrese número compra");
  } else {
    $("#numero_c_obligg").html("");
  }

  if (iva.length == 0 || iva.trim() == "") {
    $("#ivaa_obligg").html("Ingrese el iva");
  } else {
    $("#ivaa_obligg").html("");
  }
}

function anular_compa_alimento(id){
  Swal.fire({
    title: "Anular la compra?",
    text: "La compra se anulará!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, anular!",
  }).then((result) => {
    if (result.isConfirmed) {
      compra_alimneto_anular(id);
    }
  });
}

function compra_alimneto_anular(id) {
  $.ajax({
    url: "/compras/compra_alimneto_anular",
    type: "POST",
    data: { id: id },
  }).done(function (response) {
    if (response > 0) {
      if (response == 1) {
        cargar_contenido('contenido_principal','/compra_alimento');
        return Swal.fire(
          "Compar anulada",
          "La compra se anulo con extio",
          "success"
        );
      }
    } else {
      return Swal.fire(
        "Error",
        "No se pudo anular la compra, error en la matrix",
        "error"
      );
    }
  });
}