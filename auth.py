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
        with open("data/passwords.txt", "r") as file:  # Use forward slashes for compatibility
            for line in file:
                stored_username, stored_password, role = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return role  # Return the role (admin or student)
    except FileNotFoundError:
        print("Error: passwords.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def get_user_details(username):
    """
    Fetch user details from users.txt based on the username.
    Returns a User object if found, otherwise None.
    """
    try:
        with open("data/users.txt", "r") as file:  # Use forward slashes for compatibility
            for line in file:
                stored_username, full_name, role = line.strip().split(",")
                if username == stored_username:
                    return User(username, full_name, role)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

