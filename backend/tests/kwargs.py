def person_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
person_info(name="Pragnesh", age=22, city="Gandhinagar")