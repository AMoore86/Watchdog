#Ultrasonic Sensor Code for Two Sensors

#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Set GPIO Pins
TRIG = 20
ECHO = 21
TRIG1 = 23
ECHO1 = 24

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Set GPIO Pins direction (IN / OUT)
print ("Distance Measurement In Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)

GPIO.output(TRIG, False)
GPIO.output(TRIG1, False)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


print ("Waiting For Sensor 1 To Send Signal")
time.sleep(2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print ("Reading")

while GPIO.input(ECHO)==0:
    pulse_start = time.time()
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)
print("Distance Sensor 1:", distance, "cm")
print ("Waiting For Sensor 2 To Send Signal")
time.sleep(2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GPIO.output(TRIG1, True)
time.sleep(0.00001)
GPIO.output(TRIG1, False)
print ("Reading Sensor 2")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while GPIO.input(ECHO1)==0:
    pulse_start = time.time()
while GPIO.input(ECHO1)==1:
    pulse_end = time.time()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pulse_duration = pulse_end - pulse_start
distance = pulse_duration *17150
distance = round(distance, 2)
print ("Distance Sensor 2:", distance, "cm")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GPIO.cleanup()




