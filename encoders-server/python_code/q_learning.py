import numpy as np
import time
import random

from python_code.robot import Robot

class QLearning():
	def __init__(self,app):
		self.app = app
		self.robot = Robot()
		self.done = False

		self.LEARNING_RATE = 0.4
		self.DISCOUNT = 0.9
		self.EPSILON = 0.9
		self.LEARNING_EPSILON = 0.002
		self.MIN_EPSILON = 0.15
		self.MAX_MOVEMENTS = 15
		self.ITERATIONS = 50
		self.ACTIONS = 4
		self.STATE_SIZE = (3,3)	

	def inicializar_q_table(self, q_table = None):
		if q_table is None:
			self.q_table = np.zeros(shape=(self.STATE_SIZE + (self.ACTIONS,)))
		else:
			assert q_table.shape == (self.STATE_SIZE + (self.ACTIONS,))
			self.q_table = q_table

	def entrenar(self):
		#for iteration in range(self.ITERATIONS):
		epsilon = self.EPSILON
		self.robot.iniciar_lectura()

		while not self.done:
			state = self.robot.reset()

			memori = False
			movements = 0
			pasos = 0
			while not memori and not self.done:
				
				if random.random() < epsilon:
					action = random.randint(0,3)
				else:
					action = np.argmax(self.q_table[state])

				if epsilon>self.MIN_EPSILON:
					epsilon-=self.LEARNING_EPSILON

				new_state,reward,memori = self.robot.step(action)


				# LA IDEA ES QUE SI VIENE AVANZANDO, NO CORTE, ENTONCES NO HAY QUE MATARLO SI HIZO MUCHOS PASOS, PORQUE PUEDE QUE ESE AVANZANDO RE PIOLA
				# podriamos hacer que done=True cuando hace 2 pasos, porque una vez avanza, sacar el brazo y seguir es parte del aprendizaje
				if reward == 1:
					pasos+=1
					movements = 0
					if pasos == 5:
						memori = True
				movements+=1
				if movements == self.MAX_MOVEMENTS:
					memori = True
					reward = -5

				max_future_q = np.max(self.q_table[new_state])
				current_q = self.q_table[state + (action, )]

				new_q = (1 - self.LEARNING_RATE) * current_q + self.LEARNING_RATE * (reward + self.DISCOUNT * max_future_q) 
				self.q_table[state + (action,)] = new_q 

				string = "State: {} - Action {} - New_State {} - Reward: {}".format(state, action,new_state,reward)
				# self.app.js.console.log(string)

				state = new_state

				self.app.js.update_table(list(self.q_table.flatten()))				

		self.robot.finalizar_lectura()
		self.robot.reposo()
		return self.q_table

	def avanzar(self):
		state = self.robot.reset()

		while not self.done:
			action = np.argmax(self.q_table[state])
			state,_,_ = self.robot.step(action)				

		self.robot.reposo()
		return self.q_table
		