from flask import Flask, render_template, request, redirect, url_for
from python_code.admin_es import AdminES

app = Flask(__name__)
adminES = AdminES()

@app.route('/')
def index():
	# Creación de una tabla Q vacía
	ROW_NUM = 3
	COL_NUM = 4
	ACT_NUM = 4 
	Q = []
	for r in range(ROW_NUM):
		row = []
		for c in range(COL_NUM):
			col = []
			for a in range(ACT_NUM):
				col.append(0)
			row.append(col)
		Q.append(row)

	# Parámetros a ser enviados al template index
	data={
		'titulo': 'Crawler Server',
		'bienvenida': 'Crawler-bot',
		'Q': Q
	}
	return render_template('index.html', data=data)


@app.route('/caminar')
def caminar():
	# Realizar un paso y redireccionar a index
	adminES.avanzar()
	return redirect(url_for('index'))

def pagina_no_encontrada(error):
	# Función que muestra el cartel de error 404
	data = {
		'titulo': 'Error 404!'
	}
	return render_template('404.html', data=data), 404

if __name__=='__main__':
	app.register_error_handler(404, pagina_no_encontrada)
	#app.run(host='0.0.0.0', port=5000)     # Para red local mediante ethernet
	app.run(host='192.168.4.1', port=5000)  # Cuando está como access point
