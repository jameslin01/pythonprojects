from tkinter import *

#lets you press numbers and it will display

def button_press(num):
    
    global equation_text

    equation_text = equation_text +str(num)

    equation_label.set(equation_text)


def equals():
    
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text=""

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text=""


def clear():
    
    global equation_text
    
    equation_label.set("")

    equation_text = ""


window = Tk()


window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg='white', width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

#Number buttons
b1 = Button(frame, text=1, height=4, width=9, font=35,
                                       command= lambda: button_press(1))
b1.grid(row=0, column=0)

b2 = Button(frame, text=2, height=4, width=9, font=35,
                                       command= lambda: button_press(2))
b2.grid(row=0, column=1)

b3 = Button(frame, text=3, height=4, width=9, font=35,
                                       command= lambda: button_press(3))
b3.grid(row=0, column=2)

b4 = Button(frame, text=4, height=4, width=9, font=35,
                                       command= lambda: button_press(4))
b4.grid(row=1, column=0)

b5 = Button(frame, text=5, height=4, width=9, font=35,
                                       command= lambda: button_press(5))
b5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))

button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

b9 = Button(frame, text=9, height=4, width=9, font=35,
                                       command= lambda: button_press(9))
b9.grid(row=2, column=2)

b0 = Button(frame, text=0, height=4, width=9, font=35,
                                       command= lambda: button_press(0))
b0.grid(row=3, column=0)

bdot = Button(frame, text=".", height=4, width=9, font=35,
                                       command= lambda: button_press("."))
bdot.grid(row=3, column=1)




#Operation buttons

bplus = Button(frame, text="+", height=4, width=9, font=35,
                                       command= lambda: button_press("+"))
bplus.grid(row=0, column=4)

bminus = Button(frame, text="-", height=4, width=9, font=35,
                                       command= lambda: button_press("-"))
bminus.grid(row=1, column=4)

btimes = Button(frame, text="x", height=4, width=9, font=35,
                                       command= lambda: button_press("x"))
btimes.grid(row=2, column=4)

bdivide = Button(frame, text="÷", height=4, width=9, font=35,
                                       command= lambda: button_press("/"))
bdivide.grid(row=3, column=4)

bequal = Button(frame, text="=", height=4, width=9, font=35,
                                       command=equals)
bequal.grid(row=3, column=2)

bclear = Button(window, text="clear", height=4, width=9, font=35,
                                       command=clear)
bclear.pack()


window.mainloop()
