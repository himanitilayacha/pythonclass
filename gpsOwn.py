import serial
from time import sleep
# For PiB+ 2, Zero use:
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
# For Pi3 use
#ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
i = 0
def gp():
	a=" "
	while True:
    		string = ser.read()
    #stringww = ser.write(str(i))
    
    		a = a + string
    #print a
    #print " : ", a.find("GPGGA")
    		if(a.count("$") == 2):
	#print a
	#sleep(4)
			if(a.find("GPGGA")>-1):
				li_gps = a.strip().split(",")
        			time_gps = int(li_gps[1][:6])

        			hour_gps = time_gps / 10000
       				min_gps  = (time_gps % 10000) / 100
				sec_gps  = (time_gps % 100)
				hour_gps, min_gps, sec_gps = str( ( hour_gps + 5 +  (min_gps + 30)/60 ) % 24), str( (min_gps + 30) % 60), str(sec_gps)

				return li_gps[2], li_gps[4], hour_gps, min_gps, sec_gps
        		a = "$"
print gp()
