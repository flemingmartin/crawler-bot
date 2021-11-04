_raspi = False

from python_code.stoppablethread import StoppableThread

if _raspi: 
	print("--- SISTEMA CARGADO EN UNA RASPI ---")
	from python_code.admin_es import AdminES
else:
	print("--- SISTEMA CARGADO EN UNA PC ---")


class Robot():
	def __init__(self):
		if _raspi: 
			self.adminES = AdminES()
		self.angulos = [0,40,75]
		self.encoders = self.lectura_encoders()
		self.recompensa = 0
		self.lectura_bloqueada = False

	def reset(self):
		self.state = [1,1]
		if _raspi:
			self.adminES.mover_servo(self.adminES.pin_servo1,self.angulos[self.state[0]])
			self.adminES.mover_servo(self.adminES.pin_servo2,self.angulos[self.state[1]])
		return tuple(self.state)

	def step(self,action):
		memori = False

		old_state = self.state.copy()

		if action == 0:
			if self.state[0]>0:
				self.state[0]-=1
			else:
				memori = True
		elif action == 1:
			if self.state[0]<(len(self.angulos)-1):
				self.state[0]+=1
			else:
				memori = True
		elif action == 2:
			if self.state[1]>0:
				self.state[1]-=1
			else:
				memori = True
		elif action == 3:
			if self.state[1]<(len(self.angulos)-1):
				self.state[1]+=1
			else:
				memori = True

		if not memori:
			if action < 2:
				# print("Mueve servo 0 a posicion " + str(self.angulos[self.state[0]]))
				if _raspi:
					self.adminES.mover_servo(self.adminES.pin_servo1,self.angulos[self.state[0]])
			else:
				# print("Mueve servo 1 a posicion " + str(self.angulos[self.state[1]]))
				if _raspi:
					self.adminES.mover_servo(self.adminES.pin_servo2,self.angulos[self.state[1]])

		
		#si hizo los movimientos pro LEER ENCODER Y VER SI AVANZÓ
		#if avanzo:
		#	reward = 1
		reward = self.recompensa
		self.lectura_bloqueada = False

		if memori: 
			reward = -4


		# if old_state == [0,1] and self.state == [0,2]:
		# 	reward = 2

		# #si me sali de la pantalla -> perdi
		# if memori or (old_state == [0,2] and self.state == [0,1]):
		# 	reward = -4

		return tuple(self.state), reward, memori

	def get_state(self):
		return tuple(self.state)

	def reposo(self):
		if _raspi:
			self.adminES.reposo()
		print("reposo")

	def iniciar_lectura(self):
		self.thread_encoders = StoppableThread(target = self.threading_function)
		self.thread_encoders.start()

	def finalizar_lectura(self):
		self.thread_encoders.stop()

	def lectura_encoders(self):
		encoders = [0,0]
		encoders[0] = self.adminES.leer_encoder(self.adminES.pin_encoder1)
		encoders[1] = self.adminES.leer_encoder(self.adminES.pin_encoder2)
		print(encoders)
		return encoders

	def calcular_avance(self, encoder):
		
		if self.encoders == encoder and not self.lectura_bloqueada:
			return 0 
		else:
			self.lectura_bloqueada = True
			return 5

	def threading_function(self):
		while not self.thread_encoders.stopped():
			encoders = self.lectura_encoders()
			self.recompensa = self.calcular_avance(encoders)
			self.encoders = encoders



	


