#import the paho.mqtt library for publish as publish
import paho.mqtt.publish as publish

#import sleep function from the time library 
from time import sleep

#initialize the value of i with 0
i=0

#for each true value
while(True):
		#increse the value of i with 1
        i=i+1

        #using the single method of publish function publish the data you want over the broker
        #for publidh the data over broker define the topic ,payload ,hostname and provide the username and password of your namespace over broker
        #always create the full accesss token for secure communication
        publish.single(topic="class_data",
                payload="Current counter is : " + str(i),
                hostname="broker.shiftr.io",
                auth = {'username': "harharhar" , 'password': "harshit123"})

