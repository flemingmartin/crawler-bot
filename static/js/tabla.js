function update_table(new_weights, state){
	/*
		Función que actualiza los valores y colores de la tabla q
		de la interfaz web. Así como también actualiza el punto
		correspondiente al estado actual. 

		Parámetros
		----------
			new_weights (array): valores actuales de la tabla q
			state (array): estado actual del robot en formato (y,x)
	*/
	var t = document.getElementById("tabla");
	var aux = [0,0,0,0]
	var rows = t.getElementsByClassName("row");
	for(var i=0; i<rows.length; i++){
		var row = rows[i];
		for (var j=0; j<row.childElementCount; j++){
			var box = row.children[j];
			var numeros = box.getElementsByClassName('numero');
			var box_style = box.getElementsByClassName('box_style')[0];
			for (var k=0; k<numeros.length; k++){
				var nuevo_numero = new_weights[k + j*numeros.length + i*numeros.length*row.childElementCount];
				numeros[k].innerHTML = nuevo_numero.toString().match(/^-?\d+(?:\.\d{0,2})?/)[0];
				aux[k] = nuevo_numero;
			}
			box_style.style.borderTopColor = "rgb("+Math.max(aux[0]*-25,0)+","+Math.max(aux[0]*25,0)+","+aux[0]+")";
			box_style.style.borderBottomColor = "rgb("+Math.max(aux[1]*-25,0)+","+Math.max(aux[1]*25,0)+","+aux[1]+")";
			box_style.style.borderLeftColor = "rgb("+Math.max(aux[2]*-25,0)+","+Math.max(aux[2]*25,0)+","+aux[2]+")";
			box_style.style.borderRightColor = "rgb("+Math.max(aux[3]*-25,0)+","+Math.max(aux[3]*25,0)+","+aux[3]+")";
		}
	}
	
	update_state(state);
}

function update_state(state){
	/*
		Función encargada de actualizar el punto de 
		estado actual en la tabla de la interfaz web 

		Parámetros
		----------
			state (array): estado actual del robot en formato (y,x)
	*/
	var x_clases = ["x0","x1","x2"];
	var y_clases = ["y0","y1","y2"];
	var estado = document.getElementById("estado");
	estado.className = "";
	estado.classList.add(x_clases[state[1]]);
	estado.classList.add(y_clases[state[0]]);
}