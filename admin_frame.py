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

        delete_button = Button(self, text="Delete", command=self.get_selected_index)
        delete_button.grid(row=3, column=5, sticky="nsew")

        # Treeview
        cols = ("Privileges", "Username", "Password", "Id")
        self.user_treeview = ttk.Treeview(self, columns=cols, show='headings')
        self.user_treeview.heading('Privileges', text='Privileges')
        self.user_treeview.heading('Username', text='Username')
        self.user_treeview.heading('Password', text='Password')
        self.user_treeview.heading('Id', text='Id')
        result = tree()

        for row in result:
            self.user_treeview.insert('', END, values=row)
        self.user_treeview.grid(row=0, column=5)

    def logout(self):
        # Switch back to the login page
        self.master.switch_to_login()

    def get_selected_index(self):
        selected_item = self.user_treeview.selection()[0]
        arr = list(selected_item)
        print(arr, "    ")
        id = int(arr[3]) -1
        print("selected id :", id)
        