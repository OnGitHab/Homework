class Person:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        person_info = f"Gender:{self.gender}, Age: {self.age}, Name: {self.first_name}, {self.last_name}"
        return person_info


class Student(Person):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"First_name: {self.first_name}, Last_name: {self.last_name},Age: {self.age}, Gender:{self.gender}, Record_book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.students_info = []

    def add_student(self, student):
        self.group.add(student)
        self.students_info.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            self.students_info.remove(student)
        else:
            print(f"Student with last name {last_name}, not found.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "/n".join(str(student) for student in self.students_info)
        return f"Number: {self.number}\n {all_students}"


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)


assert str(gr.find_student("Jobs")) == str(st1)
assert gr.find_student("Jobs2") is None
assert isinstance(gr.find_student("Jobs"), Student) is True

gr.delete_student("Taylor")
print(gr)
