
class Employee:
    def __init__(self, name, email, role):
    self.name = name 
    self.email = email
    self.role = role

    def show_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Role: {self.role}")

emp1 = Employee("Yash", "Yash@gmail.com", "Admin")
emp2 = Employee("Parth", "Parth@gmail.com", "Editor")

emp1.show_info()
emp2.show_info()

    