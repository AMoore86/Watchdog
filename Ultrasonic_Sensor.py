
#Ultrasonic Sensor Code for Two Sensors

#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Set GPIO Pins
TRIG = 16
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

# Set TRIG to HIGH (True)
GPIO.output(TRIG, True)

# Set TRIG after 0.01ms to LOW (False)
time.sleep(0.00001)
GPIO.output(TRIG, False)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print ("Reading")

# Save StartTime
while GPIO.input(ECHO)==0:
    pulse_start = time.time()
    
# Save time of arrival
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate distance by using Speed = [Distance / Time]
# 343m/s is speed of sound at sea level
# 34300 = [Distance / (Time / 2)]
# 17150 = [Distance / Time]
# 17150 * Time = Distance

# Time Difference between start and arrival 
pulse_duration = pulse_end - pulse_start

# Multiply with the sonic speed 
distance1 = pulse_duration * 17150

# Round Distance to two decimal places 
distance1 = round(distance1, 2)

def getDist1 ():
    return distance1


# Print Distance of Ultrasonic 1
print("Distance Sensor 1:", distance1, "cm")
print ("Waiting For Sensor 2 To Send Signal")
time.sleep(2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set TRIG1 to HIGH (True)
GPIO.output(TRIG1, True)

# Set TRIG1 after 0.01ms to LOW (False)
time.sleep(0.00001)
GPIO.output(TRIG1, False)
print ("Reading Sensor 2")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Save StartTime
while GPIO.input(ECHO1)==0:
    pulse_start = time.time()
    
# Save time of arrival
while GPIO.input(ECHO1)==1:
    pulse_end = time.time()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Calculate distance by using Speed = [Distance / Time]
# 343m/s is speed of sound at sea level
# 34300 = [Distance / (Time / 2)]
# 17150 = [Distance / Time]
# 17150 * Time = Distance

# Time Difference between start and arrival 
pulse_duration = pulse_end - pulse_start

# Multiply with the sonic speed 
distance2 = pulse_duration *17150

# Round Distance to two decimal places 
distance2 = round(distance2, 2)

def getDist2():
    return distance2

# Print Distance of Ultrasonic 2
print ("Distance Sensor 2:", distance2, "cm")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






GPIO.cleanup()






