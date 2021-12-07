$(function(){
  $('#Avanzar').click(function(){
    $('#Avanzar').addClass("hidden");
    $('#Detener').removeClass("hidden");
    $('#Entrenar').addClass("hidden");
    $('#No_Entrenar').removeClass("hidden");
    $('#Reset').addClass("hidden");
    $('#No_Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Avanzando";
  });
  $('#Detener').click(function(){
    $('#Detener').addClass("hidden");
    $('#Avanzar').removeClass("hidden");
    $('#No_Entrenar').addClass("hidden");
    $('#Entrenar').removeClass("hidden");
    $('#No_Reset').addClass("hidden");
    $('#Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
  });
  $('#Entrenar').click(function(){
    $('#Entrenar').addClass("hidden");
    $('#Finalizar').removeClass("hidden");
    $('#Avanzar').addClass("hidden");
    $('#No_Avanzar').removeClass("hidden");
    $('#Reset').addClass("hidden");
    $('#No_Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Entrenando";
  });
  $('#Finalizar').click(function(){
    $('#Finalizar').addClass("hidden");
    $('#Entrenar').removeClass("hidden");
    $('#No_Avanzar').addClass("hidden");
    $('#Avanzar').removeClass("hidden");
    $('#No_Reset').addClass("hidden");
    $('#Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
  });
  $('#abrir_menu').click(function(){
    $('#menu').removeClass("hidden");
    $('#menu').removeClass("fadeOutRight");
    $('#menu').addClass("fadeInRight");
  })
  $('#cerrar_menu').click(function(){
    $('#menu').removeClass("hidden");
    $('#menu').removeClass("fadeInRight");
    $('#menu').addClass("fadeOutRight");
  })
})

// OTRA ALTERNATIVA 
function estado_avanzando(){
  // $('#Avanzar').css("display", "none");
  // $('#No_Avanzar').css("display", "none");
  // $('#Detener').css("display", "block");

  // $('#Entrenar').css("display", "none");
  // $('#No_Entrenar').css("display", "block");
  // $('#Finalizar').css("display", "none");

  // $('#Reset').css("display", "none");
  // $('#No_Reset').css("display", "block");

  // var contenido = document.getElementById("Estado").innerText = "Estado: Avanzando";
}

function estado_detenido_entrenar(){
  // $('#Avanzar').css("display", "block");
  // $('#No_Avanzar').css("display", "none");
  // $('#Detener').css("display", "none");

  // $('#Entrenar').css("display", "block");
  // $('#No_Entrenar').css("display", "none");
  // $('#Finalizar').css("display", "none");

  // $('#Reset').css("display", "block");
  // $('#No_Reset').css("display", "none");

  // var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
}

function estado_entrenando(){
  // $('#Avanzar').css("display", "none");
  // $('#No_Avanzar').css("display", "block");
  // $('#Detener').css("display", "none");

  // $('#Entrenar').css("display", "none");
  // $('#No_Entrenar').css("display", "none");
  // $('#Finalizar').css("display", "block");

  // $('#Reset').css("display", "none");
  // $('#No_Reset').css("display", "block");

  // var contenido = document.getElementById("Estado").innerText = "Estado: Entrenando";
}

function estado_detenido_finalizar(){
  // $('#Avanzar').css("display", "block");
  // $('#No_Avanzar').css("display", "none");
  // $('#Detener').css("display", "none");

  // $('#Entrenar').css("display", "block");
  // $('#No_Entrenar').css("display", "none");
  // $('#Finalizar').css("display", "none");

  // $('#Reset').css("display", "block");
  // $('#No_Reset').css("display", "none");
  // var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
}