import urllib2 as browser
import RPi.GPIO as G

G.setwarnings(False)
G.setmode(G.BCM)
G.setup(18,G.OUT)

try:
	while(True):
		content = browser.urlopen("http://class.aarmontech.com/2/bulb.txt")
		bulb =  content.read() 
		print bulb
		if(bulb == '1'):
			print "Glow"
			G.output(18,True)
		else:
			print "Not Glow"
			G.output(18,False)
except:
	G.cleanup()
