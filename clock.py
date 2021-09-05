from tkinter import *
from tkinter.ttk import *


from time import strftime

root= Tk()
root.title("Clock - by Aditya")

timeLabel = Label(root, font=("ds-digital", 80), background="black", foreground = "green" )
timeLabel.pack(anchor="center")


def time():
    string = strftime('%H:%M:%S %p')
    timeLabel.config(text=string)
    timeLabel.after(1000, time)

time()

mainloop()
