from tkinter import *

root = Tk()

#This creates a label widget
theLabel1 = Label(root, text="Hello world")
theLabel2 = Label(root, text="My name is Aditya. Im doing Python")

theLabel1.grid(row=0, column=0)
theLabel2.grid(row=1, column=1)
root.mainloop()
