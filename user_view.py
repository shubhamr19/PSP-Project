import tkinter as tk
from tkinter import messagebox
from auth import authenticate, get_user_details


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


