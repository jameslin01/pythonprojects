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

# Window dimensions

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

dnFrame = Frame(window, width = 300, height = 290, bg=c1, relief = 'raised')
dnFrame.grid(row=2, column=0)

# Logo and app name ----------------------------------------------------------

img = Image.open('/icon.png')
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

# Middle frame  --------------------------------------------------------------

app_income = Label(mdFrame, text = 'Monthly income after-tax?', height = 1, anchor = NW, font = ('Ivy 10'),
                 bg = c1, fg = c4)
app_income.place(x = 7, y = 15)

# Input income after-tax

e_value = Entry(mdFrame, width = 10, font = ('Ivy 14'), justify = 'center', relief = 'solid')
e_value.place(x = 10, y = 40)

b_calculate = Button(mdFrame, anchor = NW, text = 'Calculate', overrelief = RIDGE,
                      font = ('Ivy 9'), justify = 'center', bg = c1, fg = c4, borderless = 1)
b_calculate.place(x = 150, y = 40)

 
                                                                                        


# Run window

window.mainloop()
