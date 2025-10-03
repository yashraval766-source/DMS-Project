class User:
    def __init__(self, username, email):
        self.username = username
        self.__email = email  # private attribute

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"User: {self.username}"

class Admin(User):
    def __init__(self, username, email, level):
        super().__init__(username, email)
        self.level = level

    def __str__(self):
        return f"Admin: {self.username}, Level: {self.level}"
