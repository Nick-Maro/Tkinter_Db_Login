from tkinter import *
from tkinter import ttk

def exit():
    global should_reopen_window1  
    should_reopen_window1 = True  
#configuring window2
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
    submit = Button(window2,width=10,height=10,foreground="green",background="green",command=exit)
    submit.grid(row=20,column=50)