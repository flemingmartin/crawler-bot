$(function(){
  $('#Avanzar').click(function(){
    $('#Avanzar').hide();
    $('#Detener').show();
    $('#Entrenar').hide();
    $('#No_Entrenar').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Avanzando";
  });
  $('#Detener').click(function(){
    $('#Detener').hide();
    $('#Avanzar').show();
    $('#No_Entrenar').hide();
    $('#Entrenar').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
  });
  $('#Entrenar').click(function(){
    $('#Entrenar').hide();
    $('#Finalizar').show();
    $('#Avanzar').hide();
    $('#No_Avanzar').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Entrenando";
  });
  $('#Finalizar').click(function(){
    $('#Finalizar').hide();
    $('#Entrenar').show();
    $('#No_Avanzar').hide();
    $('#Avanzar').show();
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
  });
})