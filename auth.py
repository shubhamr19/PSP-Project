import os


class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role


def authenticate(username, password):
    """
    Authenticate the user by checking the credentials in passwords.txt.
    Returns the role (admin or student) if valid, otherwise None.
    """
    try:
        with open("data/passwords.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) != 3:  # Validate the number of fields
                    print(f"Invalid line format in passwords.txt: {line.strip()}")
                    continue
                stored_username, stored_password, role = fields
                if username == stored_username and password == stored_password:
                    return role  # Return the role (admin or student)
    except FileNotFoundError:
        print("Error: passwords.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def get_student_grades(username):
    """
    Fetch grades for a student from grades.txt.
    Returns a dictionary of subjects and grades if found, otherwise None.
    """
    try:
        with open("data/grades.txt", "r") as file:
            for line in file:
                stored_username, *grades = line.strip().split(",")
                if username == stored_username:
                    return grades  # Return the grades as a list
    except FileNotFoundError:
        print("Error: grades.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def get_student_eca(username):
    """
    Fetch extracurricular activities for a student from eca.txt.
    Returns a list of activities if found, otherwise None.
    """
    try:
        with open("data/eca.txt", "r") as file:
            for line in file:
                stored_username, *activities = line.strip().split(",")
                if username == stored_username:
                    return activities  # Return the activities as a list
    except FileNotFoundError:
        print("Error: eca.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def update_student_profile(username, full_name):
    """
    Update the student's profile information in users.txt.
    """
    try:
        updated = False
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                stored_username, _, role = line.strip().split(",")
                if username == stored_username:
                    file.write(f"{username},{full_name},{role}\n")
                    updated = True
                else:
                    file.write(line)
        return updated
    except Exception as e:
        print(f"Error: {e}")
        return False
