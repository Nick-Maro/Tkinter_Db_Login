from tkinter import *
from tkinter import ttk
from db import check,cursor_
class LoginFrame(Frame):
    def __init__(self, master, switch_to_admin):
        super().__init__(master)

        self.master = master
        self.switch_to_admin = switch_to_admin

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

        
        if check(username,password,cursor_):
            self.switch_to_admin()
        else:
            print("Invalid credentials")

class AdminFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Create UI elements for the admin page
        Label(self, text="Admin Panel", font=("Arial", 24)).grid(row=0, column=0, sticky="nsew")
        Label(self, text="Admin-specific content or functionalities here").grid(row=1, column=0, sticky="nsew")

        logout_button = Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=0, sticky="nsew")

    def logout(self):
        # Switch back to the login page
        self.master.switch_to_login()

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Frame-Based Page Switcher")
        self.geometry("600x400")

        # Create frames for login and admin pages
        self.login_frame = LoginFrame(self, self.switch_to_admin)
        self.admin_frame = AdminFrame(self)

        # Initially, show only the login frame
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.admin_frame.grid_forget()

    def switch_to_admin(self):
        self.login_frame.grid_forget()
        self.admin_frame.grid(row=0, column=0, sticky="nsew")

    def switch_to_login(self):
        self.admin_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky="nsew")

   #mainloop
if __name__ == "__main__":
    app = App()
    app.mainloop()