(function() {
	window.inputNumber = function(el) {
		/*
		  	Recibe una lista de elementos y ejecuta la función init para cada uno

		  	Parámetros
		  	----------
				el (array): lista de elementos a modificar
		*/
		el.each(function() { // Por cada elemento se ejecuta init
			init($(this));
		});

		function init(el) {
			/* 
				Recibe un elemento, configura los botones - y + para el 
				anterior y siguiente respectivamente. 
				
				Parámetros
				----------
					el: elemento correspondiente a un input-number
			*/
			var min = el.attr('min');
			var max = el.attr('max');
			var step = parseFloat(el.attr('step'));
			var presicion = Math.log10(step)*-1

			var els = {};
			els.dec = el.prev();
			els.inc = el.next();

			els.dec.on('click', decrement);
			els.inc.on('click', increment);

			function decrement() {
				/*
					Función utilizada para decrementar el valor de input-number.
					Tiene en cuenta el valor mínimo, la precisión y el step asignados. 
				*/
				var value = parseFloat(el[0].value);
				var new_value = value-step;
				if (new_value >= min){
					if (new_value > max){
						new_value = parseFloat(max);
					}
					el[0].value = new_value.toFixed(presicion);
				}
		  	}

			function increment() {
				/*
					Función utilizada para decrementar el valor de input-number.
					Tiene en cuenta el valor máximo, la precisión y el step asignados. 
				*/
				var value = parseFloat(el[0].value);
				var new_value = value+step;
				if (new_value <= max){
					if (new_value < min){
						new_value = parseFloat(min);
					}
					el[0].value = new_value.toFixed(presicion);
				}
			}
		}
	}
})();

inputNumber($('.input-number')); // Asigna el comportamiento de los botones a cada elemento de la clase input-number