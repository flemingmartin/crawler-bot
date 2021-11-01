//alert('Hola usuario del Crawler mágico')

function hola(){
  console.log("Hola");
}

function desaparecerEntrenar(){
	document.getElementById("entrenar").style.display = "none"
	document.getElementById("detener").style.display = "block"
}

function desaparecerDetener(){
	document.getElementById("detener").style.display = "none"
	document.getElementById("entrenar").style.display = "block"
}