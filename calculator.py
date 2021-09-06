##########################################################################################
##                                                                                      ##
##  MIT License                                                                         ##
##                                                                                      ##
##  Copyright (c) 2021 AdityaAparadh                                                    ##
##                                                                                      ##
##  Permission is hereby granted, free of charge, to any person obtaining a copy        ##
##  of this software and associated documentation files (the "Software"), to deal       ##
##  in the Software without restriction, including without limitation the rights        ##
##  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell           ##
##  copies of the Software, and to permit persons to whom the Software is               ##
##  furnished to do so, subject to the following conditions:                            ##
##                                                                                      ##
##  The above copyright notice and this permission notice shall be included in all      ##
##  copies or substantial portions of the Software.                                     ##
##                                                                                      ##
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR          ##
##  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,            ##
##  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE         ##
##  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER              ##
##  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,       ##
##  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE       ##
##  SOFTWARE.                                                                           ##
##                                                                                      ##
##########################################################################################

#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------


# CHANGELOG:
#
#
# v.0.05
# Addition now works
# Clear now works
# Equals to button now works
#
#
# v0.1
# subtraction, multiplication, and divison now works
#
#
# v0.2
# Added logbox and operatorbox
#
# v0.2.5
# Added a copy of MIT License
# Added this CHANGELOG
# Added KNOWN ISSUES

# v0.3
# Now it supports float calculations seamlessly

#v0.4
#Added a decimal button

#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------


# KNOWN ISSUES

# Unesessarily converts integers into floats

# If we enter a single no. and press equals to, it returns an error

# Two operators consecutively pressed causes error

#Doesn't have seperate buttons for All Clear and Delete

# UI is ugly





#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
# v 0.4


from tkinter import *

root = Tk()
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------


root.title("Calculator - by Aditya ")
root.configure(background='#131313')


#First the input

calcInput = Entry(root, width=8,font = ('Century Gothic', 35, 'bold'), foreground='#FFFFFF', background='#131313')
calcInput.grid(row=1 , column=0, columnspan=3, padx=10 , pady=10)


logbox = Entry(root, width=10, font = ('Century Gothic', 20, 'bold'), foreground='#FFFFFF', background='#131313')
logbox.grid(row=0, column=0, columnspan=2)

operatorbox = Entry(root, width=2, font = ('Century Gothic', 20, 'bold'), foreground='#FFFFFF', background='#131313')
operatorbox.grid(row=0, column=2)




# Now the BUTTONS

def Button_click(number):

    current= calcInput.get()
    calcInput.delete(0, END)
    calcInput.insert(0, (current + str(number)))
    button_add["state"] = NORMAL
    button_subtract["state"] = NORMAL
    button_multiply["state"] = NORMAL
    button_divide["state"] = NORMAL
    button_calc["state"] = NORMAL
    return


def Button_clear():
    calcInput.delete(0, END)
    logbox.delete(0, END)
    operatorbox.delete(0, END)
    return


def Button_add():
    button_add["state"] = DISABLED
    button_subtract["state"] = DISABLED
    button_multiply["state"] = DISABLED
    button_divide["state"] = DISABLED
    button_calc["state"] = DISABLED
    logbox.delete(0,END)
    operatorbox.delete(0,END)
    first_number= calcInput.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    logbox.insert(0, f_num)
    operatorbox.insert(0, '+')
    calcInput.delete(0, END)
    return

def Button_subtract():
    button_add["state"] = DISABLED
    button_subtract["state"] = DISABLED
    button_multiply["state"] = DISABLED
    button_divide["state"] = DISABLED
    button_calc["state"] = DISABLED
    logbox.delete(0,END)
    operatorbox.delete(0,END)
    first_number= calcInput.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    logbox.insert(0, f_num)
    operatorbox.insert(0, '-')

    calcInput.delete(0, END)
    return

def Button_multiply():
    button_add["state"] = DISABLED
    button_subtract["state"] = DISABLED
    button_multiply["state"] = DISABLED
    button_divide["state"] = DISABLED
    button_calc["state"] = DISABLED
    logbox.delete(0,END)
    operatorbox.delete(0,END)
    first_number= calcInput.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    logbox.insert(0, f_num)
    operatorbox.insert(0, 'x')
    calcInput.delete(0, END)
    return

def Button_divide():
    button_add["state"] = DISABLED
    button_subtract["state"] = DISABLED
    button_multiply["state"] = DISABLED
    button_divide["state"] = DISABLED
    button_calc["state"] = DISABLED
    logbox.delete(0,END)
    operatorbox.delete(0,END)
    first_number= calcInput.get()
    global f_num
    global math
    math = "divison"
    f_num = float(first_number)
    logbox.insert(0, f_num)
    operatorbox.insert(0, '/')
    calcInput.delete(0, END)
    return

def Button_equal():
    second_number= calcInput.get()
    calcInput.delete(0, END)
    logbox.delete(0, END)
    operatorbox.delete(0, END)

    if math == "addition":
        calcInput.insert(0, f_num + float(second_number))
    if math == "subtraction":
        calcInput.insert(0, f_num - float(second_number))
    if math =="multiplication":
        calcInput.insert(0, f_num * float(second_number))
    if math == "divison":
        calcInput.insert(0, f_num / float(second_number))

    return

button_1 = Button(root, text="1" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=21, pady=10, command=lambda: Button_click(1))

button_2 = Button(root, text="2" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=20, pady=10, command=lambda: Button_click(2))

button_3 = Button(root, text="3" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=20, pady=10, command=lambda: Button_click(3))

button_4 = Button(root, text="4" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=21, pady=10, command=lambda: Button_click(4))

button_5 = Button(root, text="5" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=20, pady=10, command=lambda: Button_click(5))

button_6 = Button(root, text="6" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=20, pady=10, command=lambda: Button_click(6))

button_7 = Button(root, text="7" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=21, pady=10, command=lambda: Button_click(7))

button_8 = Button(root, text="8" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=20, pady=10, command=lambda: Button_click(8))

button_9 = Button(root, text="9" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=20, pady=10, command=lambda: Button_click(9))

button_0 = Button(root, text="0" ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=21, pady=10, command=lambda: Button_click(0))

button_decimal = Button(root, text="." ,font = ('Century Gothic', 20), foreground='#FFFFFF', background='#060606', padx=20, pady=10, command=lambda: Button_click("."))


button_1.grid(row=4 , column=0 )
button_2.grid(row=4 , column=1 )
button_3.grid(row=4 , column=2 )

button_4.grid(row=3 , column=0 )
button_5.grid(row=3 , column=1 )
button_6.grid(row=3 , column=2 )

button_7.grid(row=2 , column=0 )
button_8.grid(row=2 , column=1 )
button_9.grid(row=2 , column=2 )

button_0.grid(row=5 , column=0 )

button_decimal.grid(row=8, column =1)


button_add = Button(root, text="+", padx=20, pady=10, command=Button_add, font = ('Century Gothic', 20), foreground='#FFFFFF', background='#131313')
button_add.grid(row=6, column=0)

button_subtract = Button(root, text="-", padx=20, pady=10, command=Button_subtract, font = ('Century Gothic', 20), foreground='#FFFFFF', background='#131313')
button_subtract.grid(row=7 , column=0)

button_multiply = Button(root, text="x", padx=20, pady=10, command=Button_multiply, font = ('Century Gothic', 20), foreground='#FFFFFF', background='#131313')
button_multiply.grid(row=7 , column=1)

button_divide = Button(root, text="/", padx=20, pady=10, command=Button_divide, font = ('Century Gothic', 20), foreground='#FFFFFF', background='#131313')
button_divide.grid(row=7 , column=2)






button_calc = Button(root, text="=", padx=40, pady=10, command=Button_equal, font = ('Century Gothic', 20), foreground='#FFFFFF', background='#131313')
button_calc.grid(row=6, column=1, columnspan=2)
button_calc["state"] = DISABLED

button_clr = Button(root, text="CLR" ,padx=41, pady=10, command =Button_clear, font = ('Century Gothic', 20), foreground='#FFFFFF', background='#131313')
button_clr.grid(row =5, column=1, columnspan=2 )




#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
