$(function(){
	/*
		Funciones codificadas utilizando JQuery
	*/
	$('#Avanzar').click(function(){
		/*
			Al hacer click en el boton avanzar, se deshabilita el resto 
			de los botones y se habilita el boton detener.
		*/
		$('#Avanzar').addClass("hidden");
		$('#Detener').removeClass("hidden");
		$('#Entrenar').addClass("hidden");
		$('#No_Entrenar').removeClass("hidden");
		$('#Reset').addClass("hidden");
		$('#No_Reset').removeClass("hidden");
		$('#Estado').text("Estado: Avanzando");

		$('.submit').prop('disabled', true);
		$('.submit').prop('title', 'El robot no puede estar avanzando');
	});
	$('#Detener').click(function(){
		/*
			Al hacer click en el boton detener, se habilitan
			los botones de control y del menú de configuración
		*/
		$('#Detener').addClass("hidden");
		$('#Avanzar').removeClass("hidden");
		$('#No_Entrenar').addClass("hidden");
		$('#Entrenar').removeClass("hidden");
		$('#No_Reset').addClass("hidden");
		$('#Reset').removeClass("hidden");
		$('#Estado').text("Estado: Detenido");

		$('.submit').prop('disabled', false);
		$('.submit').prop('title', "");
	});
	$('#Entrenar').click(function(){
		/*
			Al hacer click en el boton entrnar, se deshabilita el resto 
			de los botones y se habilita el boton detener.
		*/
		$('#Entrenar').addClass("hidden");
		$('#Finalizar').removeClass("hidden");
		$('#Avanzar').addClass("hidden");
		$('#No_Avanzar').removeClass("hidden");
		$('#Reset').addClass("hidden");
		$('#No_Reset').removeClass("hidden");
		$('#Estado').text("Estado: Entrenando");

		$('.submit').prop('disabled', true);
		$('.submit').prop('title', 'El robot no puede estar entrenando');
	});
	$('#Finalizar').click(function(){
		/*
			Al hacer click en el boton detener, se habilitan
			los botones de control y del menú de configuración
		*/
		$('#Finalizar').addClass("hidden");
		$('#Entrenar').removeClass("hidden");
		$('#No_Avanzar').addClass("hidden");
		$('#Avanzar').removeClass("hidden");
		$('#No_Reset').addClass("hidden");
		$('#Reset').removeClass("hidden");
		$('#Estado').text("Estado: Detenido");

		$('.submit').prop('disabled', false);
		$('.submit').prop('title', "");
	});
	$('#abrir_menu').click(function(e){
		/*
			Al hacer click en el botón de menú, se realiza la animación de apertura

			Si se clickea fuera del recuadro de menú, se mostrará la animación de cierre
		*/
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
		/*
			Al hacer click en el botón cerrar menú, se realiza la animación de cierre
		*/
		$('#oscuridad').fadeOut(1000);
		$('#menu').removeClass("hidden");
		$('#menu').removeClass("fadeInRight");
		$('#menu').addClass("fadeOutRight");
	})
})