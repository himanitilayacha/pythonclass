# import the library that allows us to logically access the GPIO pins
# refer to the library as G, it is like an alias
import RPi.GPIO as R

#import the time and sleep function from time library that allow us to provide delay
from time import time,sleep

import paho.mqtt.publish as p

#To disable warning of channel is already in use
R.setwarnings(False)

# use the BOARD numbering scheme or we can use BCM scheme also
R.setmode(R.BOARD)

# set pin 12 in output mode in direction OUT and
# set pi                        n 16 in input mode in direction IN
R.setup(12,R.OUT)
R.setup(16,R.IN)
R.setup(7,R.OUT)
R.setup(37,R.OUT)

# Define the trigger pin and echo pin on 12 and 16 pin respectively
Triger_pin = 12
Echo_pin = 16
led = 7
#define distance function which gives us the object distance
while True:
	#we initialize the trigger pin after each 1msec
	R.output(Triger_pin,True)
	sleep(0.00001)
	R.output(Triger_pin,False)

	#using time function from time library record the start and end time of the signal from ultrasonic sensor
	start_time = time()
	end_time = time()

	#when we not recieve any signal at echo pin do 
	while(R.input(Echo_pin) == 0):
		start_time = time()

	#when we recieve signal at the echo pin do
	while(R.input(Echo_pin) == 1):
		end_time = time()

	#calculate the duration by subtracting the start time by the end time
	#now use this duration time to calculate the distance by using the formula for distance calculation
	#i.e. distance = time * speed
	#Here we use the air as the transmission medium so the speed of the wave is 34300 m/sec
	#To calculate the objet distance we will divide the total distance by 2 to get the distnce between sensoor and object
	duration = end_time - start_time
	distance = (duration * 34300)/2
	print distance

	#using the single method of publish function publish the data you want over the broker
    	#for publidh the data over broker define the topic ,payload ,hostname and provide the username and password of your namespace over broker
    	#always create the full accesss token for secure communication
	if(distance >= 100):
		R.output(led,True)
		R.output(37,True)
		print "HIGH"
	elif(distance <= 5):
		R.output(37,False)
		print "LOW"
	continue
	p.single(topic = "water_level",
                payload = str(distance),
                hostname="broker.shiftr.io",
                auth={"username":'rinkirinki',"password":'himanihimani'})
