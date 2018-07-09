import serial
from time import sleep

ser = serial.Serial("/dev/serial0", 9600, timeout=1)

while True:
	val = ser.read(12)
	print val
	sleep(1)
#	i = int(val)
#	if val == i:
#		print val
#	else:
#		print("Excess Denied")
