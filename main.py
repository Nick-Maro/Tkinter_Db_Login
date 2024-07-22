from tkinter import *


# Import login and admin frames
from login_frame import LoginFrame
from admin_frame import AdminFrame
from user_frame import UserFrame
class App(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Frame-Based Page Switcher")
        self.geometry("600x400")
        # Create instances of login and admin frames
        self.login_frame = LoginFrame(self, self.switch_to_admin,self.switch_to_user)
        self.admin_frame = AdminFrame(self)
        self.user_frame = UserFrame(self)
        # Initially, show only the login frame
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.admin_frame.grid_forget()
        self.user_frame.grid_forget()

        #login -> admin
    def switch_to_admin(self):
        self.login_frame.grid_forget()
        self.admin_frame.grid(row=0, column=0, sticky="nsew")
        #login -> user
    def switch_to_user(self):
        self.login_frame.grid_forget()
        self.user_frame.grid(row=0,column=0,sticky="nsew")
        #admin -> login
    def switch_to_login(self):
        self.admin_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        #user -> login
    def switch_to_login_user(self):
        self.user_frame.grid_forget()
        self.login_frame.grid(row=0,column=0,sticky="nsew")
if __name__ == "__main__":
    app = App()
    app.mainloop()