from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.before_request
def before_request():
	print("Antes de la petición")

@app.after_request
def after_request(response):
	print("Despues de la petición")
	return response

@app.route('/')
def index():
	acciones=['Caminar', 'Correr', 'Aprender', 'Manejarse con la mente']
	data={
		'titulo': 'Crawler Feliz',
		'bienvenida': '¡Saludos!',
		'acciones': acciones,
		'cant_acciones': len(acciones)
	}
	return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
	data = {
		'titulo': 'Contacto',
		'nombre': nombre,
		'edad': edad
	}
	return render_template('contact.html', data=data)

def query_string():
	print(request)
	print(request.args)
	print(request.args.get('param1'))
	print(request.args.get('param2'))
	return "Ok"

def pagina_no_encontrada(error):
	data = {
		'titulo': 'Error 404!'
	}
	return render_template('404.html', data=data), 404
	#return redirect(url_for('index'))

if __name__=='__main__':
	app.add_url_rule('/query_string', view_func=query_string)
	app.register_error_handler(404, pagina_no_encontrada)
	#app.run(debug=True, port=8888)
	#app.run(host='192.168.1.38', port=8888)
	app.run(host='0.0.0.0', port=8888)