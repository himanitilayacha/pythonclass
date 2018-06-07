import urllib2 as browser
from requests import get
while(1):
        temperature = raw_input("Enter temperature : ")
        myURL = "https://class.aarmontech.com/25/?temprature=" + temperature
        i = get(myURL)


   



