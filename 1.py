from tkinter import *

root = Tk()

#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------


#LABELS

#This creates a label widget
theLabel1 = Label(root, text="Hello world")
theLabel2 = Label(root, text="My name is Aditya. Im doing Python")

#This is how we can position widgets in the grid
theLabel1.grid(row=0, column=0)
theLabel2.grid(row=1, column=1)


#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

#BUTTONS

#Lets define a general python function the button could call into
def buttonClick():
    clickLabel = Label(root, text="You clicked a button")
    clickLabel.grid(row=2, column=2)

#Now we'll define buttons
myButton = Button(root, text="Button", padx=200, pady= 200, command = buttonClick, fg="red", bg="green")
myButton.grid(row=0, column=1)

#Here padx and pady are used to define the size of buttons in pixels
#Here "command" is used to define the command to execute in case the button is clicked
#bg and fg are used to define background and foreground color respectively for the button


#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------


root.mainloop()
