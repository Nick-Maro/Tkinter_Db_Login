from tkinter import *
from tkinter import ttk

row=100 #number of rows
col=100 #number of columns

window = Tk()
window.geometry("600x600")
window.title("Prova")
window.resizable(True,True)


window.grid()
for i in range(row):
    window.rowconfigure(i, weight=1)
for i in range(col):
    window.columnconfigure(i, weight=1)
username = StringVar()
username_entry = ttk.Entry(window, textvariable=username,width=50)
username_entry.grid(row=5,column=50,)


if __name__ == "__main__":
    window.mainloop()