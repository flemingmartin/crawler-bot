import time
import pigpio

class AdminCaminar: 
	def __init__(self):
		'''
			Constructor de la clase AdminCaminar
		'''

		# Conectar con Raspi local
		self.pi = pigpio.pi()
        
		# Pines digitales asociados a cada dispositivo
		self.pin_servo1 = 23
		self.pin_servo2 = 24
		self.pin_encoder1 = 20
		self.pin_encoder2 = 21

		# Se establecen los pines en modo entrada o salida
		self.pi.set_mode(self.pin_servo1, pigpio.OUTPUT)
		self.pi.set_mode(self.pin_servo2, pigpio.OUTPUT)
		self.pi.set_mode(self.pin_encoder1, pigpio.INPUT)
		self.pi.set_mode(self.pin_encoder2, pigpio.INPUT)

	def _mover_servo(self, pin, angulo):
		'''
			Función que realiza el movimiento de un servomotor
			Parametros
			----------
				pin: 	int - número de pin de datos del servomotor
				angulo: int - ángulo de rotación del servomotor indicado
		'''
		ancho = (angulo*2000)/180 + 500
		self.pi.set_servo_pulsewidth(pin, ancho)
		time.sleep(0.5)

	def avanzar(self):
		'''
			Función que realiza un paso del crawler-bot y luego detiene los motores
		'''

		# Luego de cada movimiento de un servo se realiza la lectura de los encoders
		self._mover_servo(self.pin_servo1, 35) 
		print("Encoder 1: ", self.pi.read(self.pin_encoder1))
		print("Encoder 2: ", self.pi.read(self.pin_encoder2))
		self._mover_servo(self.pin_servo2, 35)
		print("Encoder 1: ", self.pi.read(self.pin_encoder1))
		print("Encoder 2: ", self.pi.read(self.pin_encoder2))
		self._mover_servo(self.pin_servo1, 0)
		print("Encoder 1: ", self.pi.read(self.pin_encoder1))
		print("Encoder 2: ", self.pi.read(self.pin_encoder2))
		self._mover_servo(self.pin_servo2, 80)
		print("Encoder 1: ", self.pi.read(self.pin_encoder1))
		print("Encoder 2: ", self.pi.read(self.pin_encoder2))

		# Posicionar en estado de reposo
		self._mover_servo(self.pin_servo1, 10)
		self._mover_servo(self.pin_servo2, 85)
		self.pi.set_servo_pulsewidth(self.pin_servo1, 0) 
		self.pi.set_servo_pulsewidth(self.pin_servo2, 0)

	#self.pi.stop() # terminate connection and release resources