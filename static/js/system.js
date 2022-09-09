function datos_usuarios_logeo() {
  $.ajax({
    type: "GET",
    url: "/usuario/datos_usuarios_logeo",
    success: function (response) {
      if (response != "" || response != null) {
        $("#nombres_l_l").html(response[1]);
        $("#rol_l").html(response[10]);
        $("#imagen_l_1").attr("src", "/static/uploads/usuario/" + response[8]);
        $("#img_l_2").attr("src", "/static/uploads/usuario/" + response[8]);

        $("#img_usuario_l").attr(
          "src",
          "/static/uploads/usuario/" + response[8]
        );
        $("#foto_actu_l").val(response[8]);

        $("#nombres_l").val(response[1]);
        $("#apellidos_l").val(response[2]);
        $("#domicilio_l").val(response[6]);
        $("#telefono_l").val(response[7]);
        $("#usuario_l").val(response[3]);

        $("#pass_oculto").val(response[4]);
      }
    },
  });
}

function mostar_perfil() {
  $("#modaleditar_usuario_logeado").modal({
    backdrop: "static",
    keyboard: false,
  });
  $("#modaleditar_usuario_logeado").modal("show");
}

function mostar_foto_l() {
  $("#modal_editar_foto_logeado").modal({
    backdrop: "static",
    keyboard: false,
  });
  $("#modal_editar_foto_logeado").modal("show");
}

function modtar_password_l() {
  $("#modaleditar_password_logeado").modal({
    backdrop: "static",
    keyboard: false,
  });
  $("#modaleditar_password_logeado").modal("show");
}

//// editar usuario
function editar_usuario_loegado() {
  var nombres = $("#nombres_l").val();
  var apellidos = $("#apellidos_l").val();
  var domicilio = $("#domicilio_l").val();
  var telefono = $("#telefono_l").val();
  var usuario = $("#usuario_l").val();

  if (
    nombres.length == 0 ||
    nombres.trim() == "" ||
    apellidos.length == 0 ||
    apellidos.trim() == "" ||
    domicilio.length == 0 ||
    domicilio.trim() == "" ||
    telefono.length == 0 ||
    telefono.trim() == "" ||
    usuario.length == 0 ||
    usuario.trim() == ""
  ) {
    validar_registros_usuario_editar_l(
      nombres,
      apellidos,
      domicilio,
      telefono,
      usuario
    );
    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#nombre_oblig_l").html("");
    $("#apellidos_obligg_l").html("");
    $("#domicilio_obligg_l").html("");
    $("#telefono_obligg_l").html("");
    $("#usuario_obligg_l").html("");
  }

  var formdata = new FormData();
  formdata.append("nombres", nombres);
  formdata.append("apellidos", apellidos);
  formdata.append("domicilio", domicilio);
  formdata.append("telefono", telefono);
  formdata.append("usuario", usuario);

  $.ajax({
    url: "/usuario/editar_usuario_logeado",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $(".modal-body").LoadingOverlay("hide");
          datos_usuarios_logeo();
          return Swal.fire(
            "Datos editados con exito",
            "Los datos del usuario se edito con exito",
            "success"
          );
        } else if (resp == 2) {
          $(".modal-body").LoadingOverlay("hide");
          return Swal.fire(
            "Usuario ya existe",
            "El usuario " + usuario + ", ya existe en el sistema",
            "warning"
          );
        }
      } else {
        $(".modal-body").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo editar el usuario, falla en la matrix",
          "error"
        );
      }
    },

    beforeSend: function () {
      $(".modal-body").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

function validar_registros_usuario_editar_l(
  nombres,
  apellidos,
  domicilio,
  telefono,
  usuario
) {
  if (nombres.length == 0 || nombres.trim() == "") {
    $("#nombre_oblig_l").html("Ingrese los nombres");
  } else {
    $("#nombre_oblig_l").html("");
  }

  if (apellidos.length == 0 || apellidos.trim() == "") {
    $("#apellidos_obligg_l").html("Ingrese los apellidos");
  } else {
    $("#apellidos_obligg_l").html("");
  }

  if (domicilio.length == 0 || domicilio.trim() == "") {
    $("#domicilio_obligg_l").html("Ingrese el domicilio");
  } else {
    $("#domicilio_obligg_l").html("");
  }

  if (telefono.length == 0 || telefono.trim() == "") {
    $("#telefono_obligg_l").html("Ingrese el telefono");
  } else {
    $("#telefono_obligg_l").html("");
  }

  if (usuario.length == 0 || usuario.trim() == "") {
    $("#usuario_obligg_l").html("Ingrese el usuario");
  } else {
    $("#usuario_obligg_l").html("");
  }
}

function editar_foto_usuario_logeado() {
  var foto = document.getElementById("foto_new_l").value;
  var ruta_actual = document.getElementById("foto_actu_l").value;

  if (foto == "" || ruta_actual.length == 0 || ruta_actual == "") {
    return swal.fire(
      "Mensaje de advertencia",
      "Ingrese una imagen para actualizar",
      "warning"
    );
  }

  var formdata = new FormData();
  var foto = $("#foto_new_l")[0].files[0];

  formdata.append("foto", foto);
  formdata.append("ruta_actual", ruta_actual);

  $.ajax({
    url: "/usuario/cambiar_foto_usuario_logeo",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $(".modal-body").LoadingOverlay("hide");
          document.getElementById("foto_new_l").value = "";
          datos_usuarios_logeo();

          return Swal.fire(
            "Foto cambiada",
            "La foto del usuario se cambio con exito",
            "success"
          );
        }
      } else {
        $(".modal-body").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "Error al cambiar la foto del usuario",
          "error"
        );
      }
    },
    beforeSend: function () {
      $(".modal-body").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

//// editar password
function editar_password_l() {
  var pass_oculto = $("#pass_oculto").val();
  var password_ac = $("#password_ac").val();
  var password_n = $("#password_n").val();
  var confirmar_p = $("#confirmar_p").val();

  if (
    password_ac.length == 0 ||
    password_ac.trim() == "" ||
    password_n.length == 0 ||
    password_n.trim() == "" ||
    confirmar_p.length == 0 ||
    confirmar_p.trim() == ""
  ) {
    validar_password(password_ac, password_n, confirmar_p);
    return swal.fire(
      "Campo vacios",
      "Los campos no deben quedar vacios, complete los datos",
      "warning"
    );
  } else {
    $("#password_ac_oblig").html("");
    $("#password_n_oblig").html("");
    $("#confirmar_p_obligg").html("");
  }

  if (pass_oculto != password_ac) {
    $("#password_ac_oblig").html("Password incorrecto");
    return swal.fire(
      "Password incorrecto",
      "El password ingresado es incorrecto",
      "error"
    );
  } else {
    $("#password_ac_oblig").html("");
  }

  if (password_n != confirmar_p) {
    $("#password_n_oblig").html("Los password no coinciden");
    $("#confirmar_p_obligg").html("Los password no coinciden");
    return swal.fire("Password", "Los password no coinciden", "warning");
  } else {
    $("#password_n_oblig").html("");
    $("#confirmar_p_obligg").html("");
  }

  if (!pass_usus_l) {
    return swal.fire(
      "Password débil",
      "Ingrese un password mas fuerte",
      "warning"
    );
  }

  var formdata = new FormData();
  formdata.append("password_n", password_n);

  $.ajax({
    url: "/usuario/cambiar_password",
    type: "POST",
    //aqui envio toda la formdata
    data: formdata,
    contentType: false,
    processData: false,
    success: function (resp) {
      if (resp > 0) {
        if (resp == 1) {
          $("#passstrength").html("");
          $("#password_ac").val("");
          $("#password_n").val("");
          $("#confirmar_p").val("");

          $(".modal-body").LoadingOverlay("hide");
          datos_usuarios_logeo();

          return Swal.fire(
            "Password editados con exito",
            "El password se edito con exito",
            "success"
          );
        }
      } else {
        $(".modal-body").LoadingOverlay("hide");
        return Swal.fire(
          "Error",
          "No se pudo editar el password, falla en la matrix",
          "error"
        );
      }
    },

    beforeSend: function () {
      $(".modal-body").LoadingOverlay("show", {
        text: "Cargando...",
      });
    },
  });
  return false;
}

function validar_password(password_ac, password_n, confirmar_p) {
  if (password_ac.length == 0 || password_ac.trim() == "") {
    $("#password_ac_oblig").html("Ingrese password actual");
  } else {
    $("#password_ac_oblig").html("");
  }

  if (password_n.length == 0 || password_n.trim() == "") {
    $("#password_n_oblig").html("Ingrese password nuevo");
  } else {
    $("#password_n_oblig").html("");
  }

  if (confirmar_p.length == 0 || confirmar_p.trim() == "") {
    $("#confirmar_p_obligg").html("Confirme password nuevo");
  } else {
    $("#confirmar_p_obligg").html("");
  }
}
