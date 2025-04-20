import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, PhotoImage
from auth import (
    authenticate, get_user_details, get_student_grades, get_student_eca,
    update_student_profile, add_user, delete_user
)

def login(username_entry, password_entry, root):
    username = username_entry.get()
    password = password_entry.get()
    role = authenticate(username, password)
    if role:
        user = get_user_details(username)
        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {user.full_name} ({user.role})!")
            if role == "admin":
                admin_dashboard(root, user)
            elif role == "student":
                student_dashboard(root, user)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def admin_dashboard(root, user):
    clear_window(root)
    root.config(bg="#f5f5f5")

    tk.Label(root, text=f"Welcome, {user.full_name}!", font=("Comic Sans MS", 20, "bold"), fg="black", bg="#f5f5f5").pack(pady=20)

    form_frame = tk.LabelFrame(root, text="Add or Edit User", padx=20, pady=20, bg="#f5f5f5", font=("Comic Sans MS", 14), fg="black")
    form_frame.pack(pady=20, padx=20, fill="x")

    labels = ["Username:", "Full Name:", "Password:", "Role:"]
    for i, label_text in enumerate(labels):
        tk.Label(form_frame, text=label_text, font=default_font, bg="#f5f5f5", fg="black").grid(row=i, column=0, sticky='e', padx=5, pady=5)

    username_entry = tk.Entry(form_frame, font=default_font)
    username_entry.grid(row=0, column=1, padx=5, pady=5)
    full_name_entry = tk.Entry(form_frame, font=default_font)
    full_name_entry.grid(row=1, column=1, padx=5, pady=5)
    password_entry = tk.Entry(form_frame, font=default_font, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    role_var = tk.StringVar(value="student")
    tk.OptionMenu(form_frame, role_var, "admin", "student").grid(row=3, column=1, padx=5, pady=5)

    def submit_user():
        username = username_entry.get()
        full_name = full_name_entry.get()
        password = password_entry.get()
        role = role_var.get()
        if add_user(username, full_name, password, role):
            messagebox.showinfo("Success", "User added/updated successfully!")
        else:
            messagebox.showerror("Error", "Failed to add/update user. Username might already exist.")

    def delete_selected_user():
        username = username_entry.get()
        if delete_user(username):
            messagebox.showinfo("Success", "User deleted successfully!")
            username_entry.delete(0, tk.END)
            full_name_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to delete user.")

    tk.Button(form_frame, text="Add/Update User", font=default_font, command=submit_user, bg="#e0aaff", fg="black").grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(form_frame, text="Delete User", font=default_font, command=delete_selected_user, bg="#ffb3c1", fg="black").grid(row=5, column=0, columnspan=2, pady=10)

    tk.Button(root, text="Logout", font=default_font, command=lambda: main_screen(root), bg="#d3f8e2", fg="black").pack(pady=10)

def student_dashboard(root, user):
    clear_window(root)
    root.config(bg="#fff0f5")

    tk.Label(root, text=f"Welcome, {user.full_name}!", font=("Comic Sans MS", 20, "bold"), fg="black", bg="#fff0f5").pack(pady=20)

    details_frame = tk.Frame(root, bg="#fff0f5")
    details_frame.pack(pady=20)

    def view_details():
        for widget in details_frame.winfo_children():
            widget.destroy()

        grades = get_student_grades(user.username)
        eca = get_student_eca(user.username)

        tk.Label(details_frame, text=f"Full Name: {user.full_name}", font=default_font, bg="#fff0f5", fg="black").pack(pady=5)
        tk.Label(details_frame, text=f"Role: {user.role}", font=default_font, bg="#fff0f5", fg="black").pack(pady=5)

        tk.Label(details_frame, text="Grades:", font=("Comic Sans MS", 14, "bold"), bg="#fff0f5", fg="black").pack(pady=(10, 0))
        if grades:
            for i, grade in enumerate(grades, 1):
                tk.Label(details_frame, text=f"Subject {i}: {grade}", font=default_font, bg="#fff0f5", fg="black").pack(pady=2)
        else:
            tk.Label(details_frame, text="No grades found.", font=default_font, bg="#fff0f5", fg="black").pack(pady=2)

        tk.Label(details_frame, text="ECA Activities:", font=("Comic Sans MS", 14, "bold"), bg="#fff0f5", fg="black").pack(pady=(10, 0))
        if eca:
            for activity in eca:
                tk.Label(details_frame, text=f"- {activity}", font=default_font, bg="#fff0f5", fg="black").pack(pady=2)
        else:
            tk.Label(details_frame, text="No extracurricular activities found.", font=default_font, bg="#fff0f5", fg="black").pack(pady=2)

    def update_profile():
        def submit():
            new_full_name = full_name_entry.get()
            if update_student_profile(user.username, new_full_name):
                messagebox.showinfo("Success", "Profile updated successfully!")
                update_window.destroy()
                user.full_name = new_full_name
                view_details()
            else:
                messagebox.showerror("Error", "Failed to update profile.")

        update_window = tk.Toplevel()
        update_window.title("Update Profile")
        update_window.geometry("300x200")
        tk.Label(update_window, text="New Full Name:", font=default_font, fg="black").pack(pady=5)
        full_name_entry = tk.Entry(update_window, font=default_font)
        full_name_entry.insert(0, user.full_name)
        full_name_entry.pack(pady=5)
        tk.Button(update_window, text="Submit", font=default_font, command=submit).pack(pady=10)

    tk.Button(root, text="View Details", font=default_font, command=view_details, bg="#c1ffd7", fg="black").pack(pady=10)
    tk.Button(root, text="Update Profile", font=default_font, command=update_profile, bg="#ffd6e0", fg="black").pack(pady=10)
    tk.Button(root, text="Logout", font=default_font, command=lambda: main_screen(root), bg="#c1c8ff", fg="black").pack(pady=10)

def main_screen(root):
    clear_window(root)
    root.config(bg="#ffd6e0")

    frame = tk.Frame(root, bg="#ffd6e0")
    frame.pack(expand=True)

    tk.Label(frame, text="Log-In", font=("Comic Sans MS", 32, "bold"), fg="#e67e8c", bg="#ffd6e0").pack(pady=20)

    tk.Label(frame, text="Username:", font=default_font, bg="#ffd6e0", fg="black").pack(pady=5)
    username_entry = tk.Entry(frame, font=default_font, bg="#eaffd0", fg="black")
    username_entry.pack(pady=5, ipady=5, ipadx=10)

    tk.Label(frame, text="Password:", font=default_font, bg="#ffd6e0", fg="black").pack(pady=5)
    password_entry = tk.Entry(frame, font=default_font, show="*", bg="#ffffcc", fg="black")
    password_entry.pack(pady=5, ipady=5, ipadx=10)

    tk.Button(frame, text="➜", font=("Comic Sans MS", 20), bg="#ffb3c1", fg="black", command=lambda: login(username_entry, password_entry, root)).pack(pady=15)

    try:
        flower_img = PhotoImage(file="flower.png")
        tk.Label(root, image=flower_img, bg="#ffd6e0").pack(pady=10)
        root.flower_img = flower_img  # keep reference
    except:
        pass

def main():
    global default_font
    root = tk.Tk()
    root.title("Login System")
    root.geometry("500x650")
    default_font = tkFont.Font(family="Comic Sans MS", size=12)
    main_screen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
