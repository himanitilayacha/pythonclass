from requests import post

i=0
from time import sleep
while True:
	print post("http://try:try@broker.shiftr.io/shaan",data="kk")
	i= i+1
	sleep(1)
