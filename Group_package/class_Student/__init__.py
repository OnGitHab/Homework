from Group_package import class_Person


class Student(class_Person.Person):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"First_name: {self.first_name}, Last_name: {self.last_name},Age: {self.age}, Gender:{self.gender}, Record_book: {self.record_book}"
