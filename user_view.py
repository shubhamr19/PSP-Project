import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":  # Example credentials
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def main():
    root = tk.Tk()
    root.title("User View")
    root.geometry("600x800")


    # Create a frame to center the elements
    frame = tk.Frame(root)
    # Center the frame both horizontally and vertically
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