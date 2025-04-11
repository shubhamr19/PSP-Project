import tkinter as tk
from tkinter import messagebox
from auth import get_student_grades, get_student_eca, update_student_profile


def student_dashboard(user):
    """
    Student dashboard functionality.
    """
    def view_details():
        """
        View personal details, grades, and extracurricular activities.
        """
        grades = get_student_grades(user.username)
        eca = get_student_eca(user.username)


        details_window = tk.Toplevel()
        details_window.title("View Details")
        details_window.geometry("400x400")


        tk.Label(details_window, text=f"Full Name: {user.full_name}", font=("Arial", 12)).pack(pady=5)
        tk.Label(details_window, text=f"Role: {user.role}", font=("Arial", 12)).pack(pady=5)


        tk.Label(details_window, text="Grades:", font=("Arial", 12, "bold")).pack(pady=5)
        if grades:
            for i, grade in enumerate(grades, 1):
                tk.Label(details_window, text=f"Subject {i}: {grade}").pack()
        else:
            tk.Label(details_window, text="No grades found.").pack()


        tk.Label(details_window, text="ECA Activities:", font=("Arial", 12, "bold")).pack(pady=5)
        if eca:
            for activity in eca:
                tk.Label(details_window, text=f"- {activity}").pack()
        else:
            tk.Label(details_window, text="No extracurricular activities found.").pack()


    def update_profile():
        """
        Update the student's profile information.
        """
        def submit():
            new_full_name = full_name_entry.get()
            if update_student_profile(user.username, new_full_name):
                messagebox.showinfo("Success", "Profile updated successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to update profile.")


        update_window = tk.Toplevel()
        update_window.title("Update Profile")
        update_window.geometry("300x200")


        tk.Label(update_window, text="New Full Name:").pack(pady=5)
        full_name_entry = tk.Entry(update_window)
        full_name_entry.insert(0, user.full_name)  # Pre-fill with current name
        full_name_entry.pack(pady=5)


        tk.Button(update_window, text="Submit", command=submit).pack(pady=10)


    student_window = tk.Toplevel()
    student_window.title("Student Dashboard")
    student_window.geometry("400x300")


    tk.Label(student_window, text=f"Welcome, {user.full_name}!", font=("Arial", 16)).pack(pady=10)


    tk.Button(student_window, text="View Details", command=view_details).pack(pady=10)
    tk.Button(student_window, text="Update Profile", command=update_profile).pack(pady=10)





