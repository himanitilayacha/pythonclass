import serial
from time import sleep
ser=serial.Serial("/dev/serial0",9600,timeout=1)
from os import system
i=0
while True:
	val=ser.read(12)
	sleep(0.1)
	if len(val.strip())==12:
		if val=="18003D96CA79":
			system("espeak -v +f3 \"permission,granted\"")
		else:
			system("espeak -v +f3 \"permission,denied\"")



