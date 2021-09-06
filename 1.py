from tkinter import *
from PIL import ImageTK,Image

root = Tk()
root.title = ("Any title")
root.iconbitmap('C:/Users/Aditya/Downloads/favicon.ico')
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------


#LABELS

#This creates a label widget
theLabel1 = Label(root, text="Hello world")
theLabel2 = Label(root, text="My name is Aditya. Im doing Python")

#This is how we can position widgets in the grid
theLabel1.grid(row=0, column=0)
theLabel2.grid(row=1, column=0)


#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

#BUTTONS

#Lets define a general python function the button could call into
def buttonClick():
    clickLabel = Label(root, text="You clicked a button")
    clickLabel.grid(row=2, column=0)

#Now we'll define buttons
myButton = Button(root, text="Button", padx=20, pady= 20, command = buttonClick, fg="red", bg="green")
myButton.grid(row=3, column=0)

#Here padx and pady are used to define the size of buttons in pixels
#Here "command" is used to define the command to execute in case the button is clicked
#bg and fg are used to define background and foreground color respectively for the button


#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

#INPUT widget


myInput = Entry(root, width=30, bg= "blue", fg="white", borderwidth=5)
myInput.grid(row=4, column=0)
myInput.insert(0, "Enter your name here")

def buttonClick2():
    label2 = Label(root, text = "Hello, " + myInput.get())
    label2.grid(row=6, column=0)


otherButton = Button(root, text="Enter", padx=20 ,pady =10, command= buttonClick2)
otherButton.grid(row=5, column=0)



# Here my input.insert is used for the default text inside the Entry
# Here myInput.get can be used to get the data in the entry for further processing


#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------



myimg = ImageTK.p



















root.mainloop()
