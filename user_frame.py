from tkinter import *



class UserFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Create UI elements for the admin page
        Label(self, text="User Panel", font=("Arial", 24)).grid(row=0, column=0, sticky="nsew")
        Label(self, text="User-specific content or functionalities here").grid(row=1, column=0, sticky="nsew")

        logout_button = Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=0, sticky="nsew")

    def logout(self):
        # Switch back to the login page
        self.master.switch_to_login_user()