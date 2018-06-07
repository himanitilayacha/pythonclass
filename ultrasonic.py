import RPi.GPIO as R
from time import time,sleep

R.setwarnings(False)
R.setmode(R.BOARD)
R.setup(12,R.OUT)
R.setup(16,R.IN)

Triger_pin = 12
Echo_pin = 16

def distance():
	R.output(Triger_pin,True)
	sleep(0.00001)
	R.output(Triger_pin,False)

	start_time = time()
	end_time = time()

	while(R.input(Echo_pin) == 0):
		start_time = time()

	while(R.input(Echo_pin) == 1):
		end_time = time()
 
	duration = end_time - start_time
	distance = (duration * 34300)/2

	return distance
while(True):
	print distance()
	sleep(1)
