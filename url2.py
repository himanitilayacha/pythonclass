import urllib2 as br
import RPi.GPIO as G
G.setmode(G.BCM)
G.setup(18,G.OUT)
while True:
	con = br.urlopen("http://class.aarmontech.com/7/bulb.txt")
	p=con.read()
	print con.read(),"a"
	if (p=='1'):
		print "true"
		G.output(18,True)
	else:
		print "false"
		G.output(18,False)
