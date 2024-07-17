from Group_package import class_Student
from Group_package import class_Group

st1 = class_Student.Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = class_Student.Student("Female", 25, "Liza", "Taylor", "AN145")
gr = class_Group.Group("PD1")
gr.add_student(st1)
gr.add_student(st2)


assert str(gr.find_student("Jobs")) == str(st1)
assert gr.find_student("Jobs2") is None
assert isinstance(gr.find_student("Jobs"), class_Student.Student) is True

gr.delete_student("Taylor")
print(gr.number)

print(gr)

