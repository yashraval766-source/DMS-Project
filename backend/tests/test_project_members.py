from backend.model.project_member import ProjectMember, Developer, Tester

def run_tests():
    pragnesh = ProjectMember("Pragnesh")
    print(pragnesh.get_role("Team Lead"))

    dev = Developer("Chirag")
    print(dev.get_role("Developer"))
    print(dev.code("Python"))

    tester = Tester("Riya")
    print(tester.get_role("Tester"))
    print(tester.test("Selenium"))

if __name__ == "__main__":
    run_tests()
