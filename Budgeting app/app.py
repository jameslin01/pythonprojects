from tkinter import *
from tkinter import Tk, ttk

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

# Creating a window 

window = Tk()
window.title('')
window.geometry('250x400')
window.configure(background=c1)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use('clam')

window.mainloop()

