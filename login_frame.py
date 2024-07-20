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
        #match password,username and see if the user has privileges
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            user_data = check(username, password, cursor_)  # Assuming check returns a tuple (user_id, is_admin)
            user_id, is_admin = user_data

            if is_admin == 1:
                print(f"{user_id} id. (Admin)")
                self.switch_to_admin()
            elif is_admin == 0:
                print(f"{user_id} id. (User)")
                self.switch_to_user()
            else:
                print("Invalid admin flag")
        except Exception as e:
            print("An error occurred:", e)
            print("Invalid credentials")