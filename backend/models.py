# models.py

class User:
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role

    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}, Role: {self.role}"
