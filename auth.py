# auth.py

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role

def authenticate(username, password):
    try:
        with open("data/passwords.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    continue
                stored_username, stored_password, _, role = [p.strip() for p in parts]
                if username == stored_username and password == stored_password:
                    return role
    except FileNotFoundError:
        print("Error: passwords.txt file not found.")
    return None

def get_user_details(username):
    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                stored_username, full_name, role = line.strip().split(",")
                if username == stored_username:
                    return User(username, full_name, role)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    return None

def get_student_grades(username):
    try:
        with open("data/grades.txt", "r") as file:
            for line in file:
                u, *grades = line.strip().split(",")
                if u == username:
                    return grades
        return []
    except FileNotFoundError:
        return []

def get_student_eca(username):
    try:
        with open("data/eca.txt", "r") as file:
            for line in file:
                stored_username, *activities = line.strip().split(",")
                if username == stored_username:
                    return activities
    except FileNotFoundError:
        print("Error: eca.txt file not found.")
    return None

def update_student_profile(username, full_name):
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

def add_user(username, full_name, password, role):
    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                stored_username, _, _ = line.strip().split(",")
                if username == stored_username:
                    return False
        with open("data/users.txt", "a") as file:
            file.write(f"{username},{full_name},{role}\n")
        with open("data/passwords.txt", "a") as file:
            file.write(f"{username},{password},{full_name},{role}\n")
        return True
    except FileNotFoundError:
        with open("data/users.txt", "w") as ufile, open("data/passwords.txt", "w") as pfile:
            ufile.write(f"{username},{full_name},{role}\n")
            pfile.write(f"{username},{password},{full_name},{role}\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def delete_user(username):
    try:
        for filename in ["data/users.txt", "data/passwords.txt"]:
            with open(filename, "r") as file:
                lines = file.readlines()
            with open(filename, "w") as file:
                for line in lines:
                    if not line.startswith(username + ","):
                        file.write(line)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
