import numpy as np
import time
import random

from python_code.robot import Robot

class QLearning():
	'''
		Clase QLearning encargada de realizar el entrenamiento
		del modelo, su inferencia y su inicialización
	'''

	def __init__(self,app):
		'''
			Constructor de la clase QLearning
		'''
		# Variables relacionadas al entrenamiento 
		self.done = False				# Indica si finalizo el entrenamiento
		self.LEARNING_RATE = 0.4		# Tasa de aprendizaje del modelo
		self.DISCOUNT = 0.9				# Factor de descuento de recompensas futuras
		self.EPSILON = 0.9				# Factor de aleatoriedad del modelo
		self.LEARNING_EPSILON = 0.002 	# Descuento de aleatoriedad
		self.MIN_EPSILON = 0.15			# Minima aleatoriedad
		self.MAX_MOVEMENTS = 15			# Maximos movimientos del brazo sin obtener recompensa
		self.ACTIONS = 4 				# Número de acciones posibles
		self.STATE_SIZE = (3,3)			# Cantidad de estados posibles
		
		# Posibles recompensas del entrenamiento
		self.WIN_REWARD = 4				# Recompensa obtenida al avanzar
		self.LOSS_REWARD = -4			# Recompensa obtenida al retroceder
		self.DEAD_REWARD = -4			# Recompensa obtenida al realizar un movimiento no permitido
		self.LOOP_REWARD = -4			# Recompensa obtenida al realizar movimientos reiterados sin obtener recompensa


		# Variable asociada a jyserver
		self.app = app

		# Instancia del agente Robot
		self.robot = Robot(self.WIN_REWARD,self.LOSS_REWARD,self.DEAD_REWARD)
		


	def inicializar_q_table(self, q_table = None):
		'''
			Inicializador de la tabla Q
			Parametros
			----------
				q_table: Recibe los valores de la tabla para ser inicializados
						 Valor por defecto: None. En este caso se inicializan todos los valores en 0
		'''
		if q_table is None:
			self.q_table = np.zeros(shape=(self.STATE_SIZE + (self.ACTIONS,)))
		else:
			assert q_table.shape == (self.STATE_SIZE + (self.ACTIONS,)) # Verificar que el tamaño de la tabla es correcto
			self.q_table = q_table

	def entrenar(self):
		'''
			Función que se encarga de realizar la lógica de entrenamiento

			Devuelve
			--------
				q_table: La tabla aprendida durante el entrenamiento
		'''

		# Inicializcion de variables y del agente
		epsilon = self.EPSILON
		self.robot.iniciar_lectura()

		# Bucle principal de entrenamiento
		while not self.done:
			# Obtener del agente el estado inicial
			state = self.robot.reset()

			dead = False	# Variable que indica si el robot realizó un movimiento no permitido
			movements = 0 	# Variable que indica la cantidad de movimientos realizados por el robot

			# Bucle de entrenamiento
			while not dead and not self.done:
				
				# Elegir accion a tomar
				if random.random() < epsilon:
					action = random.randint(0,3)	# Accion aleatoria
				else:
					action = np.argmax(self.q_table[state])	# Mejor acción segun el modelo

				# Decremento de la aleatoriedad
				if epsilon>self.MIN_EPSILON:
					epsilon-=self.LEARNING_EPSILON

				# Realizar la accion en el agente y recibir nuevo estado, 
				# recompensa y si realizo movimiento no permitido
				new_state,reward,dead = self.robot.step(action)

				# Incrementa la cantidad de movimientos
				movements+=1

				# Si el robot avanzo, se resetean la cantidad de movimientos
				if reward == self.WIN_REWARD:
					movements = 0

				# Si se realizaron el numero maximo de movimientos sin 
				# obtener recompensa -> el robot se encuentra en un bucle
				if movements == self.MAX_MOVEMENTS:
					dead = True
					reward = self.LOOP_REWARD # Asignar recompensa negativa

				
				# Calculos relacionados a la ecuacion utilizada por el modelo QLearning
				max_future_q = np.max(self.q_table[new_state]) 	# Mejor valor Q futuro
				current_q = self.q_table[state + (action, )]	# Valor Q actual

				# Ecuacion de aprendizaje
				new_q = (1 - self.LEARNING_RATE) * current_q + self.LEARNING_RATE * (reward + self.DISCOUNT * max_future_q) 
				
				# Actualizacion del valor de la tabla
				self.q_table[state + (action,)] = new_q

				# Debug
				# string = "State: {} - Action {} - New_State {} - Reward: {}".format(state, action,new_state,reward)
				# self.app.js.console.log(string)

				# Actualizacion del estado
				state = new_state

				# Actualizacion de la tabla mediante manejo del DOM
				self.app.js.update_table(list(self.q_table.flatten()))				

		# Terminar la ejecucion del robot y llevar a un estado de reposo
		self.robot.finalizar_lectura()
		self.robot.reposo()

		# Retornar la tabla aprendida
		return self.q_table

	def avanzar(self):
		'''
			Función que se encarga de utilizar el modelo para que el crawler avance
		'''
		# Llevar al robot a un estado inicial
		state = self.robot.reset()

		# Bucle principal encargado de realizar el procesamiento
		while not self.done:
			action = np.argmax(self.q_table[state])	# Tomar la mejor accion segun el modelo
			state,_,_ = self.robot.step(action)		# Realizar la accion en el agente

		# Llevar al robot a un estado de reposo
		self.robot.reposo()
		