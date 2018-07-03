from Tkinter import *
import random as r
import RPi.GPIO as G
from time import sleep

color=['red','blue','green','brown','black','purple']

w=Tk()
w.geometry("360x360")
w.configure(background ='maroon')
w.title('project')

G.setmode(G.BOARD)
G.setup(12,G.OUT)

def glow():

        G.output(12,True)
	sleep(0.01)
        w.configure(bg=color[r.randint(0,8)])

button1=Button(w,width=15 , text="ON",command=glow)
button1.grid(row=1,column=1)

def dim():

        G.output(12,False)
        w.configure(bg=color[r.randint(0,8)])

button2=Button(w,width=15 ,text="OFF", command=dim)
button2.grid(row=2,column=1)

s=Label(w,width=10,text="Data")
s.grid(row=3,column=1)

sa=Entry(w,width=10)
sa.grid(row=3,column=3)
w.mainloop()
