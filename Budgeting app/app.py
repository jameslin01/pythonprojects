# Importing tkinter

from tkinter import *
from tkinter import Tk, ttk
from tkmacosx import Button


# Importing pillow

from PIL import Image, ImageTk

# Colours

c0 = "#2e2d2b"
c1 = "#feffff"
c2 = "#4fa882"
c3 = "#38576b"
c4 = "#403d3d"
c5 = "#e06636"
c6 = "#038cfc"
c7 = "#3fbfb9"
c8 = "#263238"
c9 = "#e9edf5"
c10 = "#6e8faf"
c11 = "#f2f4f2"

# Creating a window ------------------------------------------------------------------

window = Tk()

# Window title

window.title('')

# Size of the window

window.geometry('250x400')
window.configure(background = c1)
window.resizable(width = FALSE, height = FALSE)

# Window style

style = ttk.Style(window)
style.theme_use('clam')

# Sections ------------------------------------------------------------------

upFrame = Frame(window, width = 300, height = 50, bg=c1, relief = 'flat')
upFrame.grid(row=0, column=0)

mdFrame = Frame(window, width = 300, height = 90, bg=c1, relief = 'solid')
mdFrame.grid(row=1, column=0)

btFrame = Frame(window, width = 300, height = 290, bg=c9, relief = 'raised')
btFrame.grid(row=2, column=0)

# Logo and app name ----------------------------------------------------------

img = Image.open('icon.png')
img = img.resize((40,40))
img = ImageTk.PhotoImage(img)

logo = Label(upFrame, image = img, width = 900, compound = LEFT,
              padx = 5, relief = FLAT, anchor = NW, bg=c1, fg = c4)
logo.place(x = 5, y = 0)

app_name = Label(upFrame, text = 'Budgeting app', compound = LEFT,
                 padx=1, relief = FLAT, anchor = NW, font = ('Verdana 18'),
                 bg = c1, fg = c4)
app_name.place(x = 60, y = 10)

# Line that seperates the first section from the second

app_line = Label(upFrame, width = 295, height = 1, anchor = NW, font = ('Verdana 1'),
                 bg = c3, fg = c1)
app_line.place(x = 0, y = 47)

# Function --------------------------------------------------------------

def calculate():

    # Getting the user income from the entry

    income = float(e_value.get())

    # Using the 50/30/20 rule we have the following percentages

    p_50 = (50/100) * income
    p_30 = (30/100) * income
    p_20 = (20/100) * income

    l_e_result['text'] = '£{:,.2f}'.format(p_50)
    l_w_result['text'] = '£{:,.2f}'.format(p_30)
    l_s_result['text'] = '£{:,.2f}'.format(p_20)

# Middle frame  --------------------------------------------------------------

app_income = Label(mdFrame, text = 'Monthly income after-tax?', height = 1, 
                   anchor = NW, font = ('Ivy 10'),bg = c1, fg = c4)
app_income.place(x = 7, y = 15)

# Input income after-tax

e_value = Entry(mdFrame, width = 10, font = ('Ivy 14'), justify = 'center',
                 relief = FLAT, bg = c1, fg = c4)
e_value.place(x = 10, y = 40)

b_calculate = Button(mdFrame, command = calculate, anchor = CENTER, text = 'Calculate', overrelief = RIDGE,
                      font = ('Ivy 9'), justify = 'center', bg = c1, fg = c4, borderless = 1)
b_calculate.place(x = 150, y = 40)

# Bottom frame 

app_name = Label(btFrame, text='Your 50/30/20 numbers', padx = 10, width = 35, height = 1, relief = FLAT,
                  anchor = NW, font=('Verdana 11'), bg = c3, fg = c1)                                                                             
app_name.place(x = 0, y = 0)

# Total Essentials

l_name = Label(btFrame, text = 'Essentials', height = 1, anchor = E, font = ('Verdana 10'),
               bg = c9, fg = c0)
l_name.place(x = 10, y = 40)

l_e_result = Label(btFrame, width = 22, height = 1, anchor = NW, font = ('Verdana 12'),
               bg = c1, fg = c4)
l_e_result.place(x = 10, y = 75)

# Total Wants

l_name = Label(btFrame, text = 'Wants', height = 1, anchor = E, font = ('Verdana 10'),
               bg = c9, fg = c0)
l_name.place(x = 10, y = 115)

l_w_result = Label(btFrame, width = 22, height = 1, anchor = NW, font = ('Verdana 12'),
               bg = c1, fg = c4)
l_w_result.place(x = 10, y = 145)

# Total Savings

l_name = Label(btFrame, text = 'Savings', height = 1, anchor = E, font = ('Verdana 10'),
               bg = c9, fg = c0)
l_name.place(x = 10, y = 185)

l_s_result = Label(btFrame, width = 22, height = 1, anchor = NW, font = ('Verdana 12'),
               bg = c1, fg = c4)
l_s_result.place(x = 10, y = 215)

# Run window

window.mainloop()
