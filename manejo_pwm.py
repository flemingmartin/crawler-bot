from RPIO import PWM          #import the library for PWM
import time                   #import time for pauses
servo=PWM.Servo()             #initialize the servo library
servo.set_servo(2,1500)       #center the MG90S
time.sleep(1)
for _i in range(10):          #loop between -90 and 90 degrees
    servo.set_servo(2,2500)
    time.sleep(1)
    servo.set_servo(2,600)
    time.sleep(1)
servo.set_servo(2,1500)
time.sleep(1)
