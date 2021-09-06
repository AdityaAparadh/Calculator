from tkinter import *
from tkinter.ttk import *


from time import strftime

root= Tk()
root.title("Clock - by Aditya")

timeLabel = Label(root, font=("Bahnschrift SemiBold", 80), background="black", foreground = "#66CA6D" )
timeLabel.pack(anchor="center")


def time():
    string = strftime('%H:%M:%S %p')
    timeLabel.config(text=string)
    timeLabel.after(1000, time)

time()

mainloop()
