from Tkinter import *
import random as r

from time import sleep

color=['red','blue','green','brown','black','purple']

w=Tk()
w.geometry("360x360")
w.configure(background ='maroon')
w.title('project')


def glow():

        w.configure(bg=color[r.randint(0,8)])

button1=Button(w,width=15 , text="ON",command=glow)
button1.grid(row=1,column=2)

def dim():

        w.configure(bg=color[r.randint(0,8)])

button2=Button(w,width=15 ,text="OFF", command=dim)
button2.grid(row=2,column=2)

s=Label(w,width=10,text="time")
s.grid(row=3,column=1)

s=Label(w,width=10,text="temperature")
s.grid(row=4,column=1)


s=Label(w,width=10,text="voltage")
s.grid(row=5,column=1)

s=Label(w,width=10,text="current")
s.grid(row=6,column=1)




sa=Entry(w,width=10)
sa.grid(row=3,column=3)

sa=Entry(w,width=10)
sa.grid(row=4,column=3)

sa=Entry(w,width=10)
sa.grid(row=5,column=3)

sa=Entry(w,width=10)
sa.grid(row=6,column=3)
w.mainloop()

