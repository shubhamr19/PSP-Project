def authenticate(username, password):
    """
    Authenticate the user with the given username and password.
    Reads credentials from the data/password.txt file.
    Returns True if credentials are valid, otherwise False.
    """
    try:
        with open("data/password.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
    except FileNotFoundError:
        print("Error: password.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return False