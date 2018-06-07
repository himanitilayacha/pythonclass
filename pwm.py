import RPi.GPIO as p
from time import sleep

p.setwarnings(False)
p.setmode(p.BOARD)
p.setup(12,p.OUT)
p.setup(7,p.OUT)
p.setup(37,p.OUT)
pwm = p.PWM(12,100)
pwm1 = p.PWM(7,100)
pwm2 = p.PWM(37,100)

dc=0
pwm.start(100)
sleep(0.01)
pwm1.start(100)
sleep(0.01)
pwm2.start(100)
sleep(0.01)

pins=[pwm,pwm1,pwm2]
i=0
c=1
try:
	while(1):
		i=i+c
		if (i < 300) and(i > 0):
			pins[int(i/100)].ChangeDutyCycle(i%100)
		else:
			c = 0 -c
		print i
		sleep(0.03)


except Exception as ex:
	pwm.stop()
	pwm1.stop()
	pwm2.stop()
finally:
	p.cleanup()

