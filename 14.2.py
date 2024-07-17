from Group_modul import Student, Group

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