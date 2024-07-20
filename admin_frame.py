from tkinter import *
from db import tree
from tkinter import ttk

class AdminFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Create UI elements for the admin page
        Label(self, text="Admin Panel", font=("Arial", 24)).grid(row=0, column=0, sticky="nsew")
        Label(self, text="Admin-specific content or functionalities here").grid(row=1, column=0, sticky="nsew")

        logout_button = Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=0, sticky="nsew")
        #Treeview
        cols = ("Privileges","Username","Password","Id")
        tab = ttk.Treeview(self,columns=cols, show='headings')
        tab.heading('Privileges', text='Privileges')
        tab.heading('Username', text='Username')
        tab.heading('Password', text='Password')
        tab.heading('Id', text='Id')
        result = tree()
        for row in result:
            tab.insert('',END,values=row)
        tab.grid(row=0,column=5)
    def logout(self):
        # Switch back to the login page
        self.master.switch_to_login()