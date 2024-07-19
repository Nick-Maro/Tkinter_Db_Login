from tkinter import *
from tkinter import ttk

row=100 #number of rows
col=100 #number of columns

window = Tk()
window.geometry("600x600")
window.title("Prova")
window.resizable(True,True)


window.grid()

#set the grid
for i in range(row):
    window.rowconfigure(i, weight=1)
for i in range(col):
    window.columnconfigure(i, weight=1)


username = StringVar()
username_entry = ttk.Entry(window, textvariable=username,width=50)
username_entry.grid(row=5,column=50)

password = StringVar()
password_entry = ttk.Entry(window, textvariable=password,width=50)
password_entry.grid(row=10,column=50)

text_1 = Label(window,text="Insert username", font=("Arial",24))
text_1.grid(row=2,column=50)

text_2 = Label(window,text="Insert password", font=("Arial",24))
text_2.grid(row=8,column=50)

submit = Button(window,width=10,height=10,foreground="green",background="green")
submit.grid(row=20,column=50)

if __name__ == "__main__":
    window.mainloop()