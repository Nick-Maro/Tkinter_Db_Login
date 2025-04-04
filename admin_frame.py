from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import tree, delete, add

class AdminFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.configure(bg="#f0f0f0")
        self.grid(padx=20, pady=20, sticky="nsew")

        for i in range(100):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)

       
        Label(self, text="Admin Panel", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=20, pady=(0, 20), sticky="nsew")

       
        Label(self, text="New User:", font=("Arial", 12), bg="#f0f0f0", fg="#555").grid(row=1, column=15, sticky="e")
        Label(self, text="Username:", font=("Arial", 12), bg="#f0f0f0", fg="#555").grid(row=1, column=16, sticky="e", padx=(10, 5))
        self.username_entry = ttk.Entry(self, font=("Arial", 12), width=15)
        self.username_entry.grid(row=1, column=17, sticky="w", padx=(0, 10))
        Label(self, text="Password:", font=("Arial", 12), bg="#f0f0f0", fg="#555").grid(row=1, column=18, sticky="e", padx=(10, 5))
        self.password_entry = ttk.Entry(self, font=("Arial", 12), show="*", width=15)
        self.password_entry.grid(row=1, column=19, sticky="w", padx=(0, 10))

        
        submit_button = ttk.Button(self, text="Add New User", command=self.submit_user)
        submit_button.grid(row=1, column=20, padx=10, pady=10, sticky="nsew")

        
        cols = ("Privileges", "Username", "Password", "Id")
        self.user_treeview = ttk.Treeview(self, columns=cols, show='headings', height=10)
        self.user_treeview.heading('Privileges', text='Privileges')
        self.user_treeview.heading('Username', text='Username')
        self.user_treeview.heading('Password', text='Password')
        self.user_treeview.heading('Id', text='Id')
        self.user_treeview.column("Privileges", anchor="center", width=100)
        self.user_treeview.column("Username", anchor="center", width=100)
        self.user_treeview.column("Password", anchor="center", width=100)
        self.user_treeview.column("Id", anchor="center", width=50)
        self.user_treeview.bind("<Button-3>", self.on_right_click)  
        self.update_tree()
        self.user_treeview.grid(row=2, column=0, columnspan=20, padx=10, pady=10, sticky="nsew")

        
        logout_button = ttk.Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        delete_button = ttk.Button(self, text="Delete Selected", command=self.delete_index)
        delete_button.grid(row=3, column=18, columnspan=3, padx=10, pady=10, sticky="nsew")

        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(20, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def update_tree(self):
        
        self.user_treeview.delete(*self.user_treeview.get_children())
        result = tree()
        for row in result:
            self.user_treeview.insert('', END, values=row)

    def logout(self):
        
        self.master.switch_to_login()

    def delete_index(self):
        try:
            selected_item = self.user_treeview.selection()[0]
            item_values = self.user_treeview.item(selected_item)['values']
            user_id = int(item_values[3])

            
            delete(user_id)
            self.update_tree()
            messagebox.showinfo("Success", "User deleted successfully")
        except IndexError:
            messagebox.showerror("Error", "No item selected")
        except ValueError:
            messagebox.showerror("Error", "Invalid ID")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def submit_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        add(username, password)
        self.update_tree()
        messagebox.showinfo("Success", "User added successfully")

    def on_right_click(self, event):
        
        item = self.user_treeview.identify_row(event.y)
        if item:
            menu = Menu(self, tearoff=0)
            menu.add_command(label="Delete", command=self.delete_index)
            menu.tk_popup(event.x_root, event.y_root)


if __name__ == "__main__":
    root = Tk()
    root.title("Admin Panel")
    root.geometry("900x600")

    frame = AdminFrame(root)
    frame.pack(expand=True, fill='both')

    root.mainloop()
