# Variable para determinar si se está ejecutando en una Raspberry o en PC. True para Raspberry
_raspi = False

if _raspi: 
	print("--- SISTEMA CARGADO EN UNA RASPI ---")
	from python_code.admin_es import AdminES
else:
	print("--- SISTEMA CARGADO EN UNA PC ---")

import random 
import time
from python_code.stoppablethread import StoppableThread
from threading import Semaphore

class Robot():
	'''
		Clase que modela el agente robot.
		Cuenta con métodos para la ejecución de acciones y administración de las recompensas.
	'''

	def __init__(self, recompensa_avanzar, recompensa_retroceder, recompensa_dead):
		'''
			Constructor de la clase Robot.
			Determina las posibles posiciones, inicializa variables y crea el
			administrador de entrada/salida si se ejecuta en Raspberry Pi

			Parametros
			----------
				recompensa_avanzar: valor asignado a la recompensa al avanzar
				recompensa_retroceder: valor asignado a la recompensa al retroceder
				recompensa_dead: valor asignado a la recompensa al intentar hacer un movimiento incorrecto
		'''
		if _raspi: 
			self.adminES = AdminES()
		self.angulos = [0,40,75]
		self.encoders = self.lectura_encoders()
		self.recompensa = 0
		self.lectura_bloqueada = False
		self.recompensa_avanzar = recompensa_avanzar
		self.recompensa_retroceder = recompensa_retroceder
		self.recompensa_dead = recompensa_dead
		self.semaforo_recompensa = Semaphore(1)
		self.semaforo_flag_bloqueo = Semaphore(1)
		self.state = [1,1]


	def reset(self):
		'''
			Metodo que sirve para el llevar al Robot al estado inicial [1,1]
			
			Devuelve
			--------
				El estado [1,1] como una tupla
		'''
		self.state = [1,1]
		if _raspi:
			self.adminES.mover_servo(self.adminES.pin_servo1,self.angulos[self.state[0]])
			self.adminES.mover_servo(self.adminES.pin_servo2,self.angulos[self.state[1]])
		return tuple(self.state)

	def step(self,action):
		'''
			Metodo encargado de la ejecución de una acción y
			devolución de parámetros útiles para el algoritmo Q-Learning
			
			Parámetros
			----------
				action: acción que debe realizar el robot
			
			Devuelve
			--------
				El estado [1,1] como una tupla
				reward: recompensa obtenida
				dead: True si el robot intentó hacer una acción incorrecta o False, en caso contrario
		'''
		dead = False

		old_state = self.state.copy()

		if action == 0:				# Accion 0: mover hacia abajo la primera articulacion
			if self.state[0]>0:
				self.state[0]-=1
			else:
				dead = True
		elif action == 1:			# Accion 1: mover hacia arriba la primera articulacion
			if self.state[0]<(len(self.angulos)-1):
				self.state[0]+=1
			else:
				dead = True
		elif action == 2:			# Accion 2: mover hacia abajo la segunda articulacion
			if self.state[1]>0:
				self.state[1]-=1
			else:
				dead = True
		elif action == 3:			# Accion 3: mover hacia arriba la segunda articulacion
			if self.state[1]<(len(self.angulos)-1):
				self.state[1]+=1
			else:
				dead = True

		if not dead:				# Si no intentó ir a una posición incorrecta, realiza la accion
			if action < 2:
				if _raspi:
					self.adminES.mover_servo(self.adminES.pin_servo1,self.angulos[self.state[0]])
			else:
				if _raspi:
					self.adminES.mover_servo(self.adminES.pin_servo2,self.angulos[self.state[1]])

		# Establece recompensa y la desbloquea para su actualización
		self.semaforo_recompensa.acquire()
		reward = self.recompensa
		self.semaforo_recompensa.release()

		self.semaforo_flag_bloqueo.acquire()
		self.lectura_bloqueada = False
		self.semaforo_flag_bloqueo.release()

		if dead: 
			reward = self.recompensa_dead

		return tuple(self.state), reward, dead

	def reposo(self):
		'''
			Metodo encargado de llevar al Robot al estado de reposo,
			mediante la ejecución de adminES.reposo() si se ejecuta en Raspberry
		'''
		if _raspi:
			self.adminES.reposo()
		print("reposo")

	def iniciar_lectura(self):
		'''
			Inicia el hilo encargado de la lectura de los encoders
		'''
		self.thread_encoders = StoppableThread(target = self.threading_function)
		self.thread_encoders.start()

	def finalizar_lectura(self):
		'''
			Detiene el hilo encargado de la lectura de los encoders
		'''
		self.thread_encoders.stop()

	def lectura_encoders(self):
		'''
			Realiza la lectura de los encoders si se ejecuta en Raspberry
			o establece valores random para los encoders, en PC.

			Devuelve
			--------
				encoders: array de dos posiciones con el valor de los encoders
		'''
		encoders = [1,1]
		if _raspi:
			encoders[0] = self.adminES.leer_encoder(self.adminES.pin_encoder1)
			encoders[1] = self.adminES.leer_encoder(self.adminES.pin_encoder2)
		else:
			encoders[0] = int(random.randint(0, 4) == 0)
			encoders[1] = int(random.randint(0, 4) == 0)
		return encoders

	def calcular_avance(self, encoder):
		'''
			Establece si el robot ha realizado un movimiento hacia atras, hacia adelante o ninguno.
			Utiliza el valor actual de los encoders y el almacenado anteriormente.

			Parametros
			----------
				encoder: valor actual de los encoders

			Devuelve
			--------
				0 -> Su no hubo cambio
				self.recompensa avanzar -> si avanzó
				self.recompensa_retroceder -> si retrocedió
		'''
		if encoder == [1,1]:  							# El valor obtenido no es útil (ambos en cero)
			self.encoders = [1,1]  						# Descartar lectura anterior
		else:
			if self.encoders == [1,1]:  				# El valor almacenado no es útil (ambos en cero)
				self.encoders == encoder  				# Sólo actualizar el nuevo valor de los encoders
			else:  										# El nuevo valor y el valor almacenado son ambos diferentes de [1,1]
				if encoder[0] > self.encoders[0]:  		# El encoder 0 pasó de 0 a 1
					self.encoders == encoder  			# Actualizar el nuevo valor de los encoders
					
					self.semaforo_flag_bloqueo.acquire()
					self.lectura_bloqueada = True  		# Bloquea el movimiento detectado hasta que sea leído
					self.semaforo_flag_bloqueo.release()
					
					# print("avance")
					return self.recompensa_avanzar		# El movimiento es hacia adelante
				if encoder[1] > self.encoders[1]:  		# El encoder 1 pasó de 0 a 1
					self.encoders == encoder  			# Actualizar el nuevo valor de los encoders
					
					self.semaforo_flag_bloqueo.acquire()
					self.lectura_bloqueada = True  		# Bloquea el movimiento detectado hasta que sea leído
					self.semaforo_flag_bloqueo.release()
					# print("retrocedi")
					return self.recompensa_retroceder	# El movimiento es hacia atrás
		return 0

	def threading_function(self):
		'''
			Función ejecutada por el StoppableThread.
			Si aun no se ha detenido el hilo, lee los encoders.
			Y luego si la variable recompensa no está bloqueada, la actualiza.
		'''
		while not self.thread_encoders.stopped():
			encoders = self.lectura_encoders()

			self.semaforo_flag_bloqueo.acquire()
			if not self.lectura_bloqueada:
				self.semaforo_flag_bloqueo.release()

				recompensa = self.calcular_avance(encoders)
				
				self.semaforo_recompensa.acquire()
				self.recompensa = recompensa
				self.semaforo_recompensa.release()
			else:
				self.semaforo_flag_bloqueo.release()				
			self.encoders = encoders