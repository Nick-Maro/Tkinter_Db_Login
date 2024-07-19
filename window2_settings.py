from tkinter import *
from tkinter import ttk


def settings_window2():
    window2 = Tk()  
    window2.title("Window 2")
    window2.geometry("600x600")
    window2.mainloop()
    row = 100
    col = 100
    for i in range(row):
        window2.rowconfigure(i, weight=1)
    for i in range(col):
        window2.columnconfigure(i, weight=1)