import tkinter as tk
from tkinter import messagebox
from auth import authenticate, get_user_details, add_user, delete_user


def admin_dashboard(user):
    """
    Admin dashboard functionality.
    """
    def add_user_ui():
        """
        UI for adding a new user.
        """
        def submit():
            new_username = username_entry.get()
            new_full_name = full_name_entry.get()
            new_password = password_entry.get()
            new_role = role_var.get()

            if add_user(new_username, new_full_name, new_password, new_role):
                messagebox.showinfo("Success", "User added successfully!")
                add_user_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add user. Username might already exist.")


        add_user_window = tk.Toplevel()
        add_user_window.title("Add User")
        add_user_window.geometry("400x300")


        tk.Label(add_user_window, text="Username:").pack(pady=5)
        username_entry = tk.Entry(add_user_window)
        username_entry.pack(pady=5)


        tk.Label(add_user_window, text="Full Name:").pack(pady=5)
        full_name_entry = tk.Entry(add_user_window)
        full_name_entry.pack(pady=5)


        tk.Label(add_user_window, text="Password:").pack(pady=5)
        password_entry = tk.Entry(add_user_window, show="*")
        password_entry.pack(pady=5)


        tk.Label(add_user_window, text="Role:").pack(pady=5)
        role_var = tk.StringVar(value="student")
        tk.OptionMenu(add_user_window, role_var, "admin", "student").pack(pady=5)


        tk.Button(add_user_window, text="Submit", command=submit).pack(pady=10)


    def delete_user_ui():
        """
        UI for deleting a user.
        """
        def submit():
            username_to_delete = username_entry.get()
            if delete_user(username_to_delete):
                messagebox.showinfo("Success", "User deleted successfully!")
                delete_user_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to delete user. Username might not exist.")


        delete_user_window = tk.Toplevel()
        delete_user_window.title("Delete User")
        delete_user_window.geometry("300x200")


        tk.Label(delete_user_window, text="Username to delete:").pack(pady=5)
        username_entry = tk.Entry(delete_user_window)
        username_entry.pack(pady=5)


        tk.Button(delete_user_window, text="Submit", command=submit).pack(pady=10)


    admin_window = tk.Toplevel()
    admin_window.title("Admin Dashboard")
    admin_window.geometry("400x300")


    tk.Label(admin_window, text=f"Welcome, {user.full_name}!", font=("Arial", 16)).pack(pady=10)


    tk.Button(admin_window, text="Add User", command=add_user_ui).pack(pady=10)
    tk.Button(admin_window, text="Delete User", command=delete_user_ui).pack(pady=10)

    


def login():
    username = username_entry.get()
    password = password_entry.get()


    # Authenticate the user
    role = authenticate(username, password)
    if role:
        user = get_user_details(username)
        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {user.full_name} ({user.role})!")
            if role == "admin":
                admin_dashboard(user)
            elif role == "student":
                student_dashboard(user)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def admin_dashboard(user):
    """
    Placeholder for admin dashboard functionality.
    """
    messagebox.showinfo("Admin Dashboard", f"Welcome to the Admin Dashboard, {user.full_name}!")


def student_dashboard(user):
    """
    Placeholder for student dashboard functionality.
    """
    messagebox.showinfo("Student Dashboard", f"Welcome to the Student Dashboard, {user.full_name}!")


def main():
    root = tk.Tk()
    root.title("Login System")
    root.geometry("400x300")


    # Create a frame to center the elements
    frame = tk.Frame(root)
    frame.pack(expand=True)


    # Username label and entry
    tk.Label(frame, text="Username:").pack(pady=5)
    global username_entry
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)


    # Password label and entry
    tk.Label(frame, text="Password:").pack(pady=5)
    global password_entry
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=5)


    # Login button
    tk.Button(frame, text="Login", command=login).pack(pady=10)


    root.mainloop()


if __name__ == "__main__":
    main()


