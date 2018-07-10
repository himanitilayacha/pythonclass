import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)

from sys import stdout


channel=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
#while True:
	#print GPIO.input(channel)

def callback(channel):
	#print GPIO.input(channel)
	if  GPIO.input(channel):
		stdout.write("\rWater not DETECTED ")
		stdout.flush()
	else:
		stdout.write("\rWater Detected     ")
		stdout.flush()
#GPIO.add_event_detect(channel ,GPIO.BOTH ,bouncetime=300)
#GPIO.add_event_callback(channel,callback)
from time import sleep
while True:
	callback(18)
	sleep(.1)
