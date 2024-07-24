from tkinter import *

class UserFrame(Frame):
    def __init__(self, master, user_id):
        super().__init__(master)

        self.master = master
        self.user_id = user_id

        # Create UI elements for the user panel
        Label(self, text="User Panel", font=("Arial", 24)).grid(row=0, column=0, sticky="nsew")
        Label(self, text=f"Welcome, User ID: {user_id}").grid(row=1, column=0, sticky="nsew")
        # Add user-specific content here

        logout_button = Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=0, sticky="nsew")

    
    def logout(self):
        # Switch back to the login page
        self.master.switch_to_login_user()
