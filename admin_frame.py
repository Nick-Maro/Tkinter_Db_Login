from tkinter import *
from db import tree, delete, add
from tkinter import ttk
from tkinter import messagebox

class AdminFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        for i in range(100):
            self.columnconfigure(i, weight=1)
        for i in range(100):
            self.rowconfigure(i, weight=1)

        # Create UI elements for the admin page
        Label(self, text="Admin Panel", font=("Arial", 24)).grid(row=0, column=0, sticky="nsew")
        Label(self, text="Admin-specific content or functionalities here").grid(row=1, column=0, sticky="nsew")

        logout_button = Button(self, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=0, sticky="nsew")

        delete_button = Button(self, text="Delete", command=self.delete_index, bg="Red")
        delete_button.grid(row=3, column=5, sticky="nsew")

        Label(self, text="Username:").grid(row=0, column=16, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=0, column=17, sticky="w")

        Label(self, text="Password:").grid(row=0, column=18, sticky="w")

        self.password_entry = Entry(self, show="*")  # Hide password input
        self.password_entry.grid(row=0, column=19, sticky="w")

        Label(self, text="New user-").grid(row=0, column=15, sticky="w")

        submit_button = Button(self, text="Add New user", command=self.submit_user, bg="Green")
        submit_button.grid(row=0, column=20, sticky="nsew")
        # Treeview
        cols = ("Privileges", "Username", "Password", "Id")
        self.user_treeview = ttk.Treeview(self, columns=cols, show='headings')
        self.user_treeview.heading('Privileges', text='Privileges')
        self.user_treeview.heading('Username', text='Username')
        self.user_treeview.heading('Password', text='Password')
        self.user_treeview.heading('Id', text='Id')
        self.user_treeview.bind("<Button-3>", self.on_right_click)
        self.update_tree()
        self.user_treeview.grid(row=0, column=5, columnspan=5)
    
        #functions
    def update_tree(self):
        self.user_treeview.delete(*self.user_treeview.get_children())  # Clear existing items
        data = tree()  # Fetch data from database
        for row in data:
            self.user_treeview.insert('', END, values=row)
        self.user_treeview.update()  # Force GUI update
        print('refreshed')
    def logout(self):
        # Switch back to the login page
        self.master.switch_to_login()

    def delete_index(self):
        try:
            selected_item = self.user_treeview.selection()[0]
            item_values = self.user_treeview.item(selected_item)['values']
            id = int(item_values[3])

            # Delete the user from the database
            delete(id)

            self.update_tree()
            #for the message
            #messagebox.showinfo("Success", "User deleted successfully")
            #
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
        #for the message
        #messagebox.showinfo("Success", "User added successfully")
        #

    def on_right_click(self, event):
        #menu on right_click
        item = self.user_treeview.item(self.user_treeview.identify("item", event.x, event.y))
        if item:
            menu = Menu(self, tearoff=0)
            menu.add_command(label="Delete", command=self.delete_index)
            menu.tk_popup(event.x, event.y)