class Robot():
	def __init__(self):
		# self.admines = AdminES()
		self.angulos = [0,40,80]

	def reset(self):
		self.state = [1,1]
		# self.admines.mover_servo(self.admines.pin_servo1,angulos[state[0]])
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
				print("Mueve servo 0 a posicion" + str(self.angulos[self.state[0]]))
				# self.admines.mover_servo(self.admines.pin_servo1,angulos[state[0]])
			else:
				print("Mueve servo 1 a posicion" + str(self.angulos[self.state[1]]))
				# self.admines.mover_servo(self.admines.pin_servo2,angulos[state[1]])

		reward = 0
		#si hizo los movimientos pro LEER ENCODER Y VER SI AVANZÓ
		#if avanzo:
		#	reward = 1
		if old_state == [1,2] and self.state == [0,2]:
			reward = 1

		#si me sali de la pantalla -> perdi
		if memori:
			reward = -1

		return tuple(self.state), reward, memori

	def render(self):
		pass
