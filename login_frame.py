from tkinter import *
from tkinter import ttk
from db import check, cursor_

class LoginFrame(Frame):
    def __init__(self, master, switch_to_admin, switch_to_user):
        super().__init__(master)

        self.master = master
        self.switch_to_admin = switch_to_admin
        self.switch_to_user = switch_to_user

        
        self.configure(bg="#f0f0f0")
        self.grid(padx=20, pady=20)

        
        Label(self, text="Login", font=("Arial", 28, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="nsew")

        
        Label(self, text="Username:", font=("Arial", 12), bg="#f0f0f0", fg="#555").grid(row=1, column=0, sticky="e", pady=10)
        self.username_entry = ttk.Entry(self, font=("Arial", 12), width=25)
        self.username_entry.grid(row=1, column=1, sticky="w", pady=10, padx=(10, 0))

        
        Label(self, text="Password:", font=("Arial", 12), bg="#f0f0f0", fg="#555").grid(row=2, column=0, sticky="e", pady=10)
        self.password_entry = ttk.Entry(self, font=("Arial", 12), show="*", width=25)
        self.password_entry.grid(row=2, column=1, sticky="w", pady=10, padx=(10, 0))

        
        login_button = ttk.Button(self, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=20, ipadx=10, ipady=5, sticky="nsew")

       
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            user_data = check(username, password, cursor_)  
            user_id, is_admin = user_data
            global current_user_id
            if is_admin == 1:
                print(f"{user_id} id. (Admin)")
                current_user_id = user_id
                self.switch_to_admin()

            elif is_admin == 0:
                current_user_id = user_id
                print(f"{user_id} id. (User)")
                self.switch_to_user(user_id)
            else:
                print("Invalid admin flag")
        
        except Exception as e:
            print("An error occurred:", e)
            Label(self, text="Retry, wrong username or password", fg="red", bg="#f0f0f0", font=("Arial", 10)).grid(row=4, column=0, columnspan=2, sticky="nsew")


if __name__ == "__main__":
    def admin_view():
        print("Switched to admin view")

    def user_view(user_id):
        print(f"Switched to user view with ID {user_id}")

    root = Tk()
    root.title("Login System")
    root.geometry("400x300")

    frame = LoginFrame(root, switch_to_admin=admin_view, switch_to_user=user_view)
    frame.pack(expand=True)

    root.mainloop()