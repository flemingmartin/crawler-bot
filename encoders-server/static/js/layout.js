function update_table(new_weights){

	var t = document.getElementById("tabla");
	var aux = [0,0,0,0]
	for(var i=0; i<t.childElementCount; i++){
		row = t.children[i];
		for (var j=0; j<row.childElementCount; j++){
			box = row.children[j];
			numeros = box.getElementsByClassName('numero');
			box_style = box.getElementsByClassName('box_style')[0];
			for (var k=0; k<numeros.length; k++){
				nuevo_numero = new_weights[k + j*numeros.length + i*numeros.length*row.childElementCount];
				numeros[k].innerHTML = nuevo_numero.toString().match(/^-?\d+(?:\.\d{0,2})?/)[0];
				aux[k] = nuevo_numero;
			}
			box_style.style.borderTopColor = "rgb("+Math.max(aux[0]*-25,0)+","+Math.max(aux[0]*25,0)+","+aux[0]+")";
			box_style.style.borderBottomColor = "rgb("+Math.max(aux[1]*-25,0)+","+Math.max(aux[1]*25,0)+","+aux[1]+")";
			box_style.style.borderLeftColor = "rgb("+Math.max(aux[2]*-25,0)+","+Math.max(aux[2]*25,0)+","+aux[2]+")";
			box_style.style.borderRightColor = "rgb("+Math.max(aux[3]*-25,0)+","+Math.max(aux[3]*25,0)+","+aux[3]+")";
		}
	}
}

numero = 0

// llave = 0

function get_numero(){
	return numero;
}

// function get_llave(){
// 	return llave;
// }