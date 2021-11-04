import time

import pigpio

pi = pigpio.pi() # Connect to local Pi.

pin = 23
# set gpio modes
pi.set_mode(pin, pigpio.OUTPUT)

# start 1500 us servo pulses on gpio2
pi.set_servo_pulsewidth(pin, 1500)
time.sleep(1)

#for _i in range(5): #loop between -90 and 90 degrees
while True: 
    pi.set_servo_pulsewidth(pin,2500)
    time.sleep(1)
    pi.set_servo_pulsewidth(pin,600)
    time.sleep(1)
    pi.set_servo_pulsewidth(pin, 1500)
    time.sleep(1)

pi.set_servo_pulsewidth(pin, 0) # stop servo pulses

pi.stop() # terminate connection and release resources
