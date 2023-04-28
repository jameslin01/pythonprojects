# Importing tkinter

from tkinter import *
from tkinter import Tk, ttk

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
window.configure(background=c1)
window.resizable(width=FALSE, height=FALSE)

# Window style

style = ttk.Style(window)
style.theme_use('clam')

# Sections ------------------------------------------------------------------

upFrame = Frame(window, width = 300, height = 50, bg=c1, relief = 'flat')
upFrame.grid(row=0, column=0)

mdFrame = Frame(window, width = 300, height = 90, bg=c2, relief = 'solid')
mdFrame.grid(row=1, column=0)

dnFrame = Frame(window, width = 300, height = 290, bg=c3, relief = 'raised')
dnFrame.grid(row=2, column=0)

# Logo ------------------------------------------------------------------

img = Image.open('logo.png')
img = img.resize((40,40))
img = ImageTk.PhotoImage(img)






# Run window

window.mainloop()
