from tkinter import *

root = Tk()
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

# This is a simple addition calculator sample from tkinter programming
root.title("Calculator")


#First the input

calcInput = Entry(root, width=35 , borderwidth = 5)
calcInput.grid(row=0 , column=0, columnspan=3, padx=10 , pady=10)


# Now the BUTTONS

def Button_click(number):

    current= calcInput.get()
    calcInput.delete(0, END)
    calcInput.insert(0, current + str(number))
    return


def Button_clear():
    calcInput.delete(0, END)
    return



button_1 = Button(root, text="1" , padx=40, pady=20, command=lambda: Button_click(1))

button_2 = Button(root, text="2" , padx=40, pady=20, command=lambda: Button_click(2))

button_3 = Button(root, text="3" , padx=40, pady=20, command=lambda: Button_click(3))

button_4 = Button(root, text="4" , padx=40, pady=20, command=lambda: Button_click(4))

button_5 = Button(root, text="5" , padx=40, pady=20, command=lambda: Button_click(5))

button_6 = Button(root, text="6" , padx=40, pady=20, command=lambda: Button_click(6))

button_7 = Button(root, text="7" , padx=40, pady=20, command=lambda: Button_click(7))

button_8 = Button(root, text="8" , padx=40, pady=20, command=lambda: Button_click(8))

button_9 = Button(root, text="9" , padx=40, pady=20, command=lambda: Button_click(9))

button_0 = Button(root, text="0" , padx=40, pady=20, command=lambda: Button_click(0))



button_1.grid(row=3 , column=0 )
button_2.grid(row=3 , column=1 )
button_3.grid(row=3 , column=2 )

button_4.grid(row=2 , column=0 )
button_5.grid(row=2 , column=1 )
button_6.grid(row=2 , column=2 )

button_7.grid(row=1 , column=0 )
button_8.grid(row=1 , column=1 )
button_9.grid(row=1 , column=2 )

button_0.grid(row=4 , column=0 )



button_add = Button(root, text="+", padx=40, pady=20, command=lambda: Button_click())
button_add.grid(row=5, column=0)

button_calc = Button(root, text="=", padx=89, pady=20, command=lambda: Button_click())
button_calc.grid(row=5, column=1, columnspan=2)

button_clr = Button(root, text="CLR" ,padx=80, pady=20, command =Button_clear)
button_clr.grid(row =4, column=1, columnspan=2 )




#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()