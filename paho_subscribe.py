#import the paho.mqtt library for subscribe as s 
import paho.mqtt.subscribe as s

#for each true value
while True:
	#using the simple method of subscribe function sunscribe the data over the broker 
	#for publidh the data over broker define the topic ,hostname and provide the username and password of your namespace over broker
	msg = s.simple(topic = "class_data",
			hostname="broker.shiftr.io",
			auth = {"username":'harharhar',"password":'harshit123'})
	print "Message is :"+msg.payload
