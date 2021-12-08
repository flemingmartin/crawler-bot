$(function(){
  $('#Avanzar').click(function(){
    $('#Avanzar').addClass("hidden");
    $('#Detener').removeClass("hidden");
    $('#Entrenar').addClass("hidden");
    $('#No_Entrenar').removeClass("hidden");
    $('#Reset').addClass("hidden");
    $('#No_Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Avanzando";
    $('.submit').prop('disabled', true);
    $('.submit').prop('title', 'El robot no puede estar avanzando');
  });
  $('#Detener').click(function(){
    $('#Detener').addClass("hidden");
    $('#Avanzar').removeClass("hidden");
    $('#No_Entrenar').addClass("hidden");
    $('#Entrenar').removeClass("hidden");
    $('#No_Reset').addClass("hidden");
    $('#Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
    $('.submit').prop('disabled', false);
    $('.submit').prop('title', "");
  });
  $('#Entrenar').click(function(){
    $('#Entrenar').addClass("hidden");
    $('#Finalizar').removeClass("hidden");
    $('#Avanzar').addClass("hidden");
    $('#No_Avanzar').removeClass("hidden");
    $('#Reset').addClass("hidden");
    $('#No_Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Entrenando";
    $('.submit').prop('disabled', true);
    $('.submit').prop('title', 'El robot no puede estar entrenando');
  });
  $('#Finalizar').click(function(){
    $('#Finalizar').addClass("hidden");
    $('#Entrenar').removeClass("hidden");
    $('#No_Avanzar').addClass("hidden");
    $('#Avanzar').removeClass("hidden");
    $('#No_Reset').addClass("hidden");
    $('#Reset').removeClass("hidden");
    var contenido = document.getElementById("Estado").innerText = "Estado: Detenido";
    $('.submit').prop('disabled', false);
    $('.submit').prop('title', "");
  });
  $('#abrir_menu').click(function(e){
    $('#oscuridad').fadeIn(1000);
    $('#menu').removeClass("hidden");
    $('#menu').removeClass("fadeOutRight");
    $('#menu').addClass("fadeInRight");

    e.stopPropagation();

    $('#menu').click(function (e) {
        e.stopPropagation();
    });
    $("html").click(function() {
      $('#oscuridad').fadeOut(1000);
      $('#menu').removeClass("hidden");
      $('#menu').removeClass("fadeInRight");
      $('#menu').addClass("fadeOutRight");    
    });
  })
  $('#cerrar_menu').click(function(){
    $('#oscuridad').fadeOut(1000);
    $('#menu').removeClass("hidden");
    $('#menu').removeClass("fadeInRight");
    $('#menu').addClass("fadeOutRight");
  })
})