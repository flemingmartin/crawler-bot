$(function(){
  $('#Avanzar').click(function(){
    $('#Avanzar').hide();
    $('#Detener').show();
    $('#Entrenar').hide();
    $('#No_Entrenar').show();
    $('#Reset').hide();
    $('#No_Reset').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Avanzando";
  });
  $('#Detener').click(function(){
    $('#Detener').hide();
    $('#Avanzar').show();
    $('#No_Entrenar').hide();
    $('#Entrenar').show();
    $('#No_Reset').hide();
    $('#Reset').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
  });
  $('#Entrenar').click(function(){
    $('#Entrenar').hide();
    $('#Finalizar').show();
    $('#Avanzar').hide();
    $('#No_Avanzar').show();
    $('#Reset').hide();
    $('#No_Reset').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Entrenando";
  });
  $('#Finalizar').click(function(){
    $('#Finalizar').hide();
    $('#Entrenar').show();
    $('#No_Avanzar').hide();
    $('#Avanzar').show();
    $('#No_Reset').hide();
    $('#Reset').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
  });
})

// OTRA ALTERNATIVA 
function estado_avanzando(){
  // $('#Avanzar').hide();
  // $('#No_Avanzar').hide();
  // $('#Detener').show();

  // $('#Entrenar').hide();
  // $('#No_Entrenar').show();
  // $('#Finalizar').hide();

  // $('#Reset').hide();
  // $('#No_Reset').show();

  // var contenido = document.getElementById("Estado").innerText = "Estado: Avanzando";
}

function estado_detenido_entrenar(){
  // $('#Avanzar').show();
  // $('#No_Avanzar').hide();
  // $('#Detener').hide();

  // $('#Entrenar').show();
  // $('#No_Entrenar').hide();
  // $('#Finalizar').hide();

  // $('#Reset').show();
  // $('#No_Reset').hide();

  // var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
}

function estado_entrenando(){
  // $('#Avanzar').hide();
  // $('#No_Avanzar').show();
  // $('#Detener').hide();

  // $('#Entrenar').hide();
  // $('#No_Entrenar').hide();
  // $('#Finalizar').show();

  // $('#Reset').hide();
  // $('#No_Reset').show();

  // var contenido = document.getElementById("Estado").innerText = "Estado: Entrenando";
}

function estado_detenido_finalizar(){
  // $('#Avanzar').show();
  // $('#No_Avanzar').hide();
  // $('#Detener').hide();

  // $('#Entrenar').show();
  // $('#No_Entrenar').hide();
  // $('#Finalizar').hide();

  // $('#Reset').show();
  // $('#No_Reset').hide();
  // var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
}