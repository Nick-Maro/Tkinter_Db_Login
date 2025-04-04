from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class UserFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.configure(bg="#f0f0f0")
        self.grid(padx=20, pady=20, sticky="nsew")

        for i in range(100):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

   
        Label(self, text="User Panel", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=20, pady=(0, 20), sticky="nsew")

       
        view_profile_button = ttk.Button(self, text="View Profile", command=self.view_profile)
        view_profile_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_profile_button = ttk.Button(self, text="Update Profile", command=self.update_profile)
        update_profile_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        change_password_button = ttk.Button(self, text="Change Password", command=self.change_password)
        change_password_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        
        logout_button = ttk.Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def view_profile(self):
        
        messagebox.showinfo("View Profile", "User profile details displayed here.")

    def update_profile(self):
        
        messagebox.showinfo("Update Profile", "User profile update functionality.")

    def change_password(self):
        
        messagebox.showinfo("Change Password", "Password change functionality.")

    def logout(self):
        
        self.master.switch_to_login_user()


if __name__ == "__main__":
    def switch_to_login_user():
        print("Switched to login user view")

    root = Tk()
    root.title("User Panel")
    root.geometry("600x400")

    frame = UserFrame(root)
    frame.pack(expand=True, fill='both')

    root.mainloop()
