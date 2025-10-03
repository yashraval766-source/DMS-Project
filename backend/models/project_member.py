from backend.helpers.logging_decorator import log_method

class ProjectMember:
    def __init__(self, name):
        self.__name = name
        self.__role = None

    @log_method
    def get_role(self, role):
        self.__role = role
        return f"{self.__name} is a {self.__role}"

class Developer(ProjectMember):
    @log_method
    def code(self, language):
        return f"{self._ProjectMember__name} is coding in {language}"

class Tester(ProjectMember):
    @log_method
    def test(self, tool):
        return f"{self._ProjectMember__name} is testing using {tool}"
