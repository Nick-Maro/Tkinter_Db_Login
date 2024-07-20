from tkinter import *

from db import check, cursor_


class LoginFrame(Frame):
    def __init__(self, master, switch_to_admin,switch_to_user):
        super().__init__(master)

        self.master = master
        self.switch_to_admin = switch_to_admin
        self.switch_to_user = switch_to_user
        
        # Create UI elements for the login page
        Label(self, text="Login", font=("Arial", 24)).grid(row=0, column=0, sticky="nsew")
        Label(self, text="Username:").grid(row=1, column=0, sticky="w")
        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, sticky="w")
        Label(self, text="Password:").grid(row=2, column=0, sticky="w")
        self.password_entry = Entry(self, show="*")  # Hide password input
        self.password_entry.grid(row=2, column=1, sticky="w")

        login_button = Button(self, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, sticky="nsew")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        #switch for admin
        if check(username, password, cursor_)[1] == 1:
            print(check(username, password, cursor_)[0]," id. (Admin)")
            self.switch_to_admin()
        #switch for user
        if check(username,password,cursor_)[1] == 0:
            print(check(username, password, cursor_)[0]," id. (User)")
            self.switch_to_user()
        else:
            print("Invalid credentials")