from tkinter import *

from tkinter import messagebox

import time, sys

from pygame import mixer

from PIL import Image, ImageTk


def alarm():

	alarm_time=user_input.get()

	if alarm_time=="":

		messagebox.askretrycancel("Error Message","Please Enter Value As per Given Statement")

	else :
        
		while True: #timer checks

			time.sleep(1)

			if (alarm_time==time.strftime("%H:%M")):

				playmusic()
           
   

def playmusic():
    
    mixer.init()
    
    mixer.music.load('Alarm.mp3')
    
    mixer.music.play() 

    time.sleep(5) #snooze time

    mixer.music.stop()

    sys.exit() 
    
	
root=Tk()

root.title("Alarm Clock with GUI")

root.geometry("400x400")

root.configure(background="blue")

canvas=Canvas(root,width=220,height=210)

img=ImageTk.PhotoImage(Image.open("Alarm.png"))

canvas.create_image(0,0,anchor=NW,image=img)

canvas.pack()

box1=Frame(root)

box1.place(x=145,y=255)

box2=Frame(root)

box2.place(x=145,y=315)

box3=Label(root,text="PLEASE SET TIME IN HR:MIN")

box3.place(x=125,y=220)

#Time taken by User as Input

user_input=Entry(box1,font=('Arial Narrow',25),width=6)

user_input.grid(row=0,column=2)

#Set Alarm Button

start_button=Button(box2,text="Set Alarm",font=('Arial Narrow',14,'bold'),command=alarm)

start_button.grid(row=2,column=2)


root.mainloop()