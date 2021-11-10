from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  
import jyserver.Flask as jsf
import numpy as np
import time
  
from python_code.q_learning import QLearning
from python_code.robot import _raspi

# Si se está ejecutando en una Raspi, 
# determinar si es en producción (False - mediante Access Point)
# o desarrollo (True - mediante cable ethernet)
if _raspi: 
	_dev = False

# Creación de la aplicación Flask y establecimiento de la base de datos 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./crawler-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

class QTable(db.Model):
	'''
		Modelo de la base de datos que establece una tabla de SQL
		donde estarán almacenadas las tablas Q entrenadas.
	'''
	__tablename__ = 'qtable'

	id = db.Column(db.Integer, primary_key=True)
	q_table = db.Column(db.PickleType, nullable=False)

	@staticmethod
	def get_by_id(id):
		return User.query.get(id)

@jsf.use(app)
class App:
	'''
		Clase que modela la aplicación Flask para su utilización con jyserver.
		Establece los metodos que pueden ser ejecutados a partir de eventos 
		producidos en la interfaz web como si de javascript se tratara. 
		De igual manera, permite la ejecución de las funciones de javascript 
		creadas, accediendo mediante self.js. 
	'''

	def __init__(self):
		'''
			Constructor de la clase App.
			Almacena una instancia de la clase QLearning y carga una tabla Q
			desde la base de datos para almacenarla como tabla inicial.
		'''
		self.Q = QLearning(self)
		
		database = QTable.query.all() 
		q_table =(database[-1].q_table)
		self.Q.inicializar_q_table(q_table)
	

	def entrenar(self):
		'''
			Función que inicia el entrenamiento y guarda la tabla Q que ha 
			sido generada tras la ejecución del mismo, en la base de datos.
		'''
		self.Q.done=False
		q_table = self.Q.entrenar()
		
		entrada_db = QTable(q_table=q_table)
		db.session.add(entrada_db)
		db.session.commit()


	def avanzar(self):
		'''
			Función que inicia el movimiento del robot utilizando la tabla
			que se encuentra almacenada en la variable Q. Que puede ser una
			recientemente entrenada o la cargada inicialmente desde la BD. 
		'''
		self.Q.done=False
		self.Q.avanzar()


	def detener(self):
		'''
			Detener la ejecución del entrenamiento o del movimiento segun corresponda.
		'''
		self.Q.done=True


	def reset_table(self):
		'''
			Función que resetea toda la tabla a 0 en Q y la actualiza en la interfaz.
		'''
		self.Q.inicializar_q_table()
		q_table = self.Q.q_table
		self.js.update_table(list(q_table.flatten()))


@app.route('/')
def index():
	'''
		Metodo correspondiente a la ruta "/" de la web.
		Se carga una entrada de la tabla para ser mostrada en la interfaz,
		además se pasan algunos parámetros a la vista. 
	'''

	database = QTable.query.all() 
	q_table =(database[-1].q_table)
	data={
		'titulo': 'Crawler Server',
		'bienvenida': 'Crawler-bot',
		'q_table': list(q_table.flatten())
	}
	return App.render(render_template('index.html', data=data))


def pagina_no_encontrada(error):
	'''
		Función que muestra el cartel de error 404
	'''
	data = {
		'titulo': 'Error 404!'
	}
	return render_template('404.html', data=data), 404


if __name__=='__main__':
	'''
		Programa principal
	'''
	app.register_error_handler(404, pagina_no_encontrada)
	if _raspi:
		if _dev:
			print(" * Red local mediante ethernet")
			app.run(host='0.0.0.0', port=5000)     # Para red local mediante ethernet
		else:
			print(" * Access point")
			app.run(host='192.168.4.1', port=5000)  # Cuando está como access point
	else:
		print(" * Run PC - Debug")
		app.run(debug=True)  # Cuando está ejecutandose en PC
