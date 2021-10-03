
# -*- coding: utf-8 -*-
###########################################################################################################IMPORTS
import pygame, sys, os
from pygame.locals import *
import numpy as np
import serial
import time
import Q_Agent_Class
import threading
from math import ceil
from db import db, Epoca, MatrizQ
###########################################################################################################OBJECTS
#ser = serial.Serial('/dev/ttyAMA0',9600,timeout=0.2)
Q_Agent = Q_Agent_Class.Q_Agent_Class()

###########################################################################################################PYGAME SETUP
# Initialize pygame
pygame.init()
pygame.font.init()
basicfont = pygame.font.SysFont(None,18)

# Set the WIDTH and HEIGHT of the screen
WINDOW_SIZE = [600, 600]

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

###########################################################################################################Q SETUP
#hyperparameters
alpha = 0.8
gamma = 0.8
epsilon = 0.9

#Q table parameters
ROW_NUM = 3
COL_NUM = 4
ACT_NUM = 4 

#runFlag for Q_Agent
Q_runFlag = False
Q_go = False
Q_runFlag_Caminar = False
Q_go_Caminar = False
GUI_enabled = False

#Reward Scheme
Fuzzy = True
Simple = False
Raw = False 
reward_threshold=10
simple_pos_val=5
simple_neg_val=-5

# Create a 3 dimensional array using the parameters 
Q = np.zeros((ROW_NUM, COL_NUM, ACT_NUM))
R = np.zeros((ROW_NUM, COL_NUM, ACT_NUM))

mQ = MatrizQ(Q=Q)
db.session.add(mQ)
db.session.commit()

#Q[2][2] = 1
Q_Agent = Q_Agent_Class.Q_Agent_Class()
crawlerDone = False


###########################################################################################################Q ALGORITHM
def RunQ():
	global Q_runFlag
	global Q_go
	global GUI_enabled
	global epsilon
	global alpha
	global gamma
	global crawlerDone
	iteration=0
	while Q_go:
		if Q_runFlag:
			if Q_Agent.S0 == 1 and Q_Agent.S1 == 3:
				Q_Agent.S0=0
				Q_Agent.S1=0
			else:

				print('iteration: ',iteration)
				Q_Agent.Policy(epsilon, ACT_NUM, Q)
				Action = Q_Agent.Take_Action(ROW_NUM, COL_NUM, ACT_NUM)
				print('Action:%s  from: %s%s   to: %s%s' %(Action, Q_Agent.S0, Q_Agent.S1, Q_Agent.S0_prime, Q_Agent.S1_prime) )
				if Action == 'out of bounds':
					print(Action)
				else:
					#ser.write(Action)
					#ser.write("\n")
					#ser.flushInput()
					#ser.flushOutput()
				
					#while(ser.inWaiting() == 0):
					#	continue
					if Q_Agent.S0 == 2 and Q_Agent.S1 == 3:
						raw_reward = 40#int(ser.readline())
					else:
						if Q_Agent.S0 == 0 and Q_Agent.S1 == 3:
							raw_reward = -100
						else:
							raw_reward = 0
					print('raw reward: ',raw_reward)
					Q_Agent.reward = parse_raw_reward(raw_reward)
					R[Q_Agent.S0][Q_Agent.S1][Q_Agent.Next_Action]=Q_Agent.reward
					print('Q reward: ', Q_Agent.reward)
				
				Q_Agent.Q_Update(Q, alpha, gamma)
				iteration=iteration+1
				# mQ = MatrizQ(Q=Q)
				# db.session.add(mQ)
				# db.session.commit()
				mQ.Q = Q
				db.session.commit()

				if GUI_enabled:

					DrawQ()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							# movido marcos
							# mQ = MatrizQ(Q=Q)
							# db.session.add(mQ)
							# db.session.commit()

							pygame.quit()
							Q_go = False

							GUI_enabled= False
							
							crawlerDone=True
							exit()
#				time.sleep(3)
		#clock.tick(10)	 # agregado marcos
	
	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	if GUI_enabled:
		pygame.quit()
###########################################################################################################caminar con lo aprendido
	
		
###########################################################################################################PARSE_RAW_REWARD		
def parse_raw_reward(raw_reward):
	global reward_threshold
	
	if Fuzzy:
		return fuzzy_reward(raw_reward)
	elif Simple:
		return simple_reward(raw_reward)
	elif Raw:
		return raw_reward
		
###########################################################################################################FUZZY_REWARD	
def fuzzy_reward(raw_reward):
	global reward_threshold
	if raw_reward > 0:
		temp = raw_reward//reward_threshold
	else:
		temp = int(ceil(float(raw_reward)/float(reward_threshold)))
	return temp
	
###########################################################################################################SIMPLE_REWARD		
def simple_reward(raw_reward):
	global reward_threshold

	if(raw_reward)>reward_threshold:
		return simple_pos_val
	elif(raw_reward)<-reward_threshold:
		return simple_neg_val	

###########################################################################################################DRAW Q-MAP
def DrawQ():
	global GUI_enabled
	global Q_go
	global Q
	global R
	global screen 
	COLOR_SCALE= 5
	
	if(GUI_enabled):
		if(Q_go):
			 # Set the screen background
			screen.fill(BLACK)
			WIDTH = (WINDOW_SIZE[0])/COL_NUM - 5
			HEIGHT = (WINDOW_SIZE[1])/ROW_NUM - 20
			for row in range(ROW_NUM):
				for column in range(COL_NUM):            
					temp = pygame.Rect((WIDTH * column + 5), (HEIGHT * row + 5),WIDTH,HEIGHT)
					
					#draw triangles for actions in each square
					
					
					Q_temp=Q[row][column]
					color = BLACK
					if Q_temp[0] > 0: color = (0,Q_temp[0]*COLOR_SCALE,0)
					elif Q_temp[0] < 0: color = (-Q_temp[0]*COLOR_SCALE,0,0)
					up = pygame.draw.polygon(screen,color,[(temp.topleft),(temp.topright),(temp.center)])
					color = BLACK            
					if Q_temp[3] > 0: color = (0,Q_temp[3]*COLOR_SCALE,0)
					elif Q_temp[3] < 0: color = (-Q_temp[3]*COLOR_SCALE,0,0)           
					right = pygame.draw.polygon(screen,color,[(temp.bottomright),(temp.topright),(temp.center)])
					color = BLACK
					if Q_temp[1] > 0: color = (0,Q_temp[1]*COLOR_SCALE,0)
					elif Q_temp[1] < 0: color = (-Q_temp[1]*COLOR_SCALE,0,0)
					down = pygame.draw.polygon(screen,color,[(temp.bottomleft),(temp.bottomright),(temp.center)])
					color = BLACK
					if Q_temp[2] > 0: color = (0,Q_temp[2]*COLOR_SCALE,0)
					elif Q_temp[2] < 0: color = (-Q_temp[2]*COLOR_SCALE,0,0)
					left = pygame.draw.polygon(screen,color,[(temp.topleft),(temp.bottomleft),(temp.center)])         
					
				
					#draw white borders
					borders_int = pygame.draw.lines(screen,WHITE,False, [(temp.topleft),(temp.bottomright),(temp.topright),(temp.bottomleft)],4)
					borders_ext = pygame.draw.rect(screen, WHITE, (temp.left,temp.top,temp.width,temp.height),2)
				
					#place agent in square that was moved to
					if (Q_Agent.S0 == row) and (Q_Agent.S1 == column):
							Agent = pygame.draw.circle(screen, BLUE, temp.center, 20)
					
					

					Qup_string = str(round(Q[row][column][0],3))
					textsurface = basicfont.render(Qup_string, False, WHITE)
					screen.blit(textsurface, up.center)
					
					Qleft_string = str(round(Q[row][column][2],3))
					textsurface = basicfont.render(Qleft_string, False, WHITE)
					screen.blit(textsurface, left.center)
					
					Qdown_string = str(round(Q[row][column][1],3))
					textsurface = basicfont.render(Qdown_string, False, WHITE)
					screen.blit(textsurface, down.center)
					
					Qright_string = str(round(Q[row][column][3],3))
					textsurface = basicfont.render(Qright_string, False, WHITE)
					screen.blit(textsurface, right.center)
					if row == 0 and column == 3:
						color=(190, 0, 0)

						cuadrado=pygame.draw.polygon(screen,color,[(temp.topleft),(temp.topright),(temp.bottomright),(temp.bottomleft)])
						textsurface = basicfont.render("-1", False, WHITE)
						screen.blit(textsurface, cuadrado.center)
						# pygame.draw.polygon(screen,color,[(temp.bottomright),(temp.topright),(temp.center)])
						# pygame.draw.polygon(screen,color,[(temp.bottomleft),(temp.bottomright),(temp.center)])
						# pygame.draw.polygon(screen,color,[(temp.topleft),(temp.bottomleft),(temp.center)])         
					elif row == 2 and column == 3:
						color=(0, 190, 0)

						
						cuadrado=pygame.draw.polygon(screen,color,[(temp.topleft),(temp.topright),(temp.bottomright),(temp.bottomleft)])
						textsurface = basicfont.render("+1", False, WHITE)
						screen.blit(textsurface, cuadrado.center)
					elif row == 1 and column == 3:
						color=BLACK
						cuadrado=pygame.draw.polygon(screen,color,[(temp.topleft),(temp.topright),(temp.bottomright),(temp.bottomleft)])
						

		# Limit to 60 frames per second
		#clock.tick(60)
		clock.tick(60) # agregado por marcos
		#time.sleep(1) # agregado por marcos
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

		
###########################################################################################################COMMAND TIMEOUT
def cmdTimeout():
	startTime = time.time()
	while(time.time() - startTime < 2.1):
		#if ser.inWaiting():
		#	break
		if time.time() - startTime > 2:
			print('Command Timeout')
			break

###########################################################################################################SINGLE MOVEMENT 
def SingleMove(RoboCmd):
	global GUI_enabled
	global Q
	global Q_Agent
	global alpha, gamma, epsilon
	Action = 0
	
	if(RoboCmd=='zero'):
		#write servos to zero position(arm tucked in)
		#ser.write(RoboCmd)
		#ser.write('\n')            
		cmdTimeout()
	else:
		if(RoboCmd=='up'):
			Action=0
		if(RoboCmd=='down'):
			Action=1
		if(RoboCmd=='left'):
			Action=2
		if(RoboCmd=='right'):
			Action=3
		Q_Agent.Next_Action = Action
		RoboCmd = Q_Agent.Take_Action(ROW_NUM, COL_NUM, ACT_NUM)
		if(RoboCmd == 'out of bounds'):
			print(RoboCmd)
		else:	
			print('Sent:', RoboCmd)
			print('Waiting on motors...')
			#ser.write(RoboCmd)
			#ser.write('\n')            
			cmdTimeout()
			#ser.flushOutput()
			#while(ser.inWaiting() == 0):
			#	continue
			raw_reward = 1 #int(ser.readline())
			print('raw reward: ',raw_reward)
			Q_Agent.reward = parse_raw_reward(raw_reward)
			R[Q_Agent.S0][Q_Agent.S1][Q_Agent.Next_Action]=Q_Agent.reward
			print('Q reward', Q_Agent.reward)
		Q_Agent.Q_Update(Q, alpha, gamma)
		if(GUI_enabled):
			DrawQ()
		
###########################################################################################################IS_NUMBER
#Checks if a string can represent a float (used in parsing)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        print("Value must be a number.")
        return False	

###########################################################################################################CHECK FOR EPSILON
#Used for changing the value of epsilon. exampleCmd: Eps = .25
def checkForEpsilon(RoboCmd):
	global epsilon
	if(RoboCmd.find('Eps') > -1):
		RoboCmd = RoboCmd.replace("Eps", "eps")
	if(RoboCmd.find('epsilon') > -1):
		RoboCmd = RoboCmd.replace("epsilon", "eps")
	if(RoboCmd.find('eps =') > -1):
		RoboCmd = RoboCmd.replace("eps =", "eps=")
		
	StartIndex = RoboCmd.find('eps=')
	if StartIndex != -1:
		if is_number(RoboCmd[StartIndex+4:len(RoboCmd)]):
			tempEps = float(RoboCmd[StartIndex+4:len(RoboCmd)])
			if (tempEps >= 0 and tempEps <= 1):
				epsilon = tempEps
				print("Epsilon is now", epsilon)
			else:
				print("Epsilon must be between 0 and 1")

###########################################################################################################CHECK FOR ALPHA
#Used for changing the value of alpha. exampleCmd: alpha = .25				
def checkForAlpha(RoboCmd):
	global alpha
	
	if(RoboCmd.find('Alpha') > -1):
		RoboCmd = RoboCmd.replace("Alpha", "alpha")
	if(RoboCmd.find('alpha =') > -1):
		RoboCmd = RoboCmd.replace("alpha =", "alpha=")
	StartIndex = RoboCmd.find('alpha=')
	if StartIndex != -1:
		if is_number(RoboCmd[StartIndex+6:len(RoboCmd)]):
			temp = float(RoboCmd[StartIndex+6:len(RoboCmd)])
			if (temp >= 0 and temp <= 1):
				alpha = temp
				print("Alpha is now", alpha)
			else:
				print("Alpha must be between 0 and 1")

###########################################################################################################CHECK FOR GAMMA
#Used for changing the value of gamma. exampleCmd: gamma = .25				
def checkForGamma(RoboCmd):
	global gamma
	
	if(RoboCmd.find('Gamma') > -1):
		RoboCmd = RoboCmd.replace("Gamma", "gamma")
	if(RoboCmd.find('gamma =') > -1):
		RoboCmd = RoboCmd.replace("gamma =", "gamma=")
	StartIndex = RoboCmd.find('gamma=')
	if StartIndex != -1:
		if is_number(RoboCmd[StartIndex+6:len(RoboCmd)]):
			temp = float(RoboCmd[StartIndex+6:len(RoboCmd)])
			if (temp >= 0 and temp <= 1):
				gamma = temp
				print("Gamma is now", gamma)
			else:
				print("Gamma must be between 0 and 1")

###########################################################################################################SHOW PARAMETERS
#Displays current parameter values				
def showParams():
    print("Epsilon =", epsilon)
    print("Alpha =", alpha)
    print("Gamma =", gamma)

	
###########################################################################################################CONTROL LOOP
screen = pygame.display.set_mode(WINDOW_SIZE)
while (not crawlerDone):
    #if ser.inWaiting()>0:
     #   print(ser.read(100))
		
    #else:
   	
    GUI_enabled = True	
    time.sleep(3)
    if Q_runFlag == False:
    	Q_runFlag = True
    	Q_go = True
    	RunQ()
    	#Qthread = threading.Thread(target = RunQ)
    	#Qthread.start()
os._exit() 