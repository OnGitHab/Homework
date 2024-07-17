class Person:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        person_info = f"Gender:{self.gender}, Age: {self.age}, Name: {self.first_name}, {self.last_name}"
        return person_info