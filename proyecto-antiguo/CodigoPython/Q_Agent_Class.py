# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:10:19 2017

@author: Edmond
"""

import numpy as np

class Q_Agent_Class(object):
    
	def __init__(self, S0=0, S1=0, S0_prime=1, S1_prime=1, Next_Action = 0, reward = 0):
		self.S0 = S0
		self.S1 = S1
		self.S0_prime = S0_prime
		self.S1_prime = S1_prime
		self.Next_Action = Next_Action
		self.reward = reward
        
	def Take_Action(self, ROW_NUM, COL_NUM, ACT_NUM):
		
		if self.Next_Action == 0:
			self.S0_prime = self.S0 - 1
			self.S1_prime = self.S1
			command = 'up'
		elif self.Next_Action == 1:
			self.S0_prime = self.S0 + 1
			self.S1_prime = self.S1 
			command = 'down'
		elif self.Next_Action == 2:
			self.S0_prime = self.S0 
			self.S1_prime = self.S1 - 1
			command = 'left'
		elif self.Next_Action == 3:
			self.S0_prime = self.S0 
			self.S1_prime = self.S1 + 1
			command = 'right'
		if self.S0_prime >= ROW_NUM or self.S0_prime < 0 or self.S1_prime >= COL_NUM or self.S1_prime < 0:
			self.reward = -10
			self.S0_prime = self.S0 
			self.S1_prime = self.S1
			command='out of bounds'
		return command  
        
	def Q_Update(self, Q, alpha, gamma):
		Q[self.S0][self.S1][self.Next_Action] = (1-alpha)*(Q[self.S0][self.S1][self.Next_Action]) + alpha*(self.reward + gamma*np.amax(Q[self.S0_prime][self.S1_prime]))
		self.S0 = self.S0_prime
		self.S1 = self.S1_prime
		
	def Policy(self, epsilon, ACT_NUM, Q):
		test = round(np.random.random(), 2)
		print(test)
		if test > epsilon:
			self.Next_Action = np.argmax(Q[self.S0][self.S1])
		else:
			self.Next_Action = np.random.randint(0,(ACT_NUM))
	# print(self.Next_Action)

	def Q_Update_Caminar(self, Q, alpha, gamma):
		#Q[self.S0][self.S1][self.Next_Action] = (1-alpha)*(Q[self.S0][self.S1][self.Next_Action]) + alpha*(self.reward + gamma*np.amax(Q[self.S0_prime][self.S1_prime]))
		self.S0 = self.S0_prime
		self.S1 = self.S1_prime