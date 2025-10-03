class ProjectMember:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

    def get_role(self):
        return self.__role

    def set_role(self, new_role):
        self.__role = new_role


class Developer(ProjectMember):
    def __init__(self, name, programming_language):
        super().__init__(name, "Developer")
        self.programming_language = programming_language

    def get_role(self):  # override
        return f"{self.get_name()} is a {super().get_role()} (works with {self.programming_language})"


class Tester(ProjectMember):
    def __init__(self, name, testing_tool):
        super().__init__(name, "Tester")
        self.testing_tool = testing_tool

    def get_role(self):  # override
        return f"{self.get_name()} is a {super().get_role()} (tests using {self.testing_tool})"
