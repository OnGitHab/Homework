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