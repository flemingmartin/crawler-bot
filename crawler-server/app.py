from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  
import jyserver.Flask as jsf
import numpy as np
import time

from python_code.robot import _raspi

if _raspi:
	from python_code.admin_es import AdminES
	adminES = AdminES()
	_dev = True

from python_code.q_learning import QLearning

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./crawler-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

class QTable(db.Model):
	__tablename__ = 'qtable'

	id = db.Column(db.Integer, primary_key=True)
	q_table = db.Column(db.PickleType, nullable=False)

	@staticmethod
	def get_by_id(id):
		return User.query.get(id)

@jsf.use(app)
class App:
	def __init__(self):
		self.Q = QLearning(self)
	
	def entrenar(self):
		self.Q.done=False

		q_table = self.Q.entrenar()
		# q_table = np.zeros((3,3,4)) # para poner una tabla vacia

		entrada_db = QTable(q_table=q_table)
		db.session.add(entrada_db)
		db.session.commit()
		print(q_table)

		# time.sleep(0.5)
		# self.js.location.reload()

	def detener(self):
		self.Q.done=True
		self.js.console.log("listorti")

	def avanzar(self):
		if _raspi:
			adminES.avanzar()
		print("avanzar")

@app.route('/')
def index():
	# Creación de una tabla Q vacía - Solo para la primera, a investigar
	# ACTIONS = 4
	# STATE_SIZE = (3,3)	
	# q_table = np.zeros(shape=(STATE_SIZE + (ACTIONS,)))
	# db.create_all()
	# database = QTable(q_table=q_table)
	# db.session.add(database)
	# db.session.commit()

	database = QTable.query.all() 
	q_table =(database[-1].q_table)

	# Parámetros a ser enviados al template index
	data={
		'titulo': 'Crawler Server',
		'bienvenida': 'Crawler-bot',
		'q_table': list(q_table.flatten())
	}
	# dola = App.render(render_template('index.html', data=data))
	# App.js.update_table(list(q_table.flatten()))
	return App.render(render_template('index.html', data=data))


# @app.route('/caminar')
# def caminar():
# 	# Realizar un paso y redireccionar a index
# 	# adminES.avanzar()
# # Agregar en la vista: <center><button href="{{url_for('caminar')}}">Avanzar</button></center>
# 	return redirect(url_for('index'))

def pagina_no_encontrada(error):
	# Función que muestra el cartel de error 404
	data = {
		'titulo': 'Error 404!'
	}
	return render_template('404.html', data=data), 404


if __name__=='__main__':
	app.register_error_handler(404, pagina_no_encontrada)
	if _raspi:
		if _dev:
			app.run(host='0.0.0.0', port=5000)     # Para red local mediante ethernet
		else:
			app.run(host='192.168.4.1', port=5000)  # Cuando está como access point
	else:
		app.run(debug=True)  # Cuando está en la compu
