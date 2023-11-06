class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []
        self.index = 0

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Error")

    def __getitem__(self, index):
        if 0 <= index < len(self.students):
            return self.students[index]
        else:
            raise IndexError()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

    def __str__(self):
        group_info = f"Group: {self.group_name}\n"
        student_list = "\n".join([str(student) for student in self.students])
        return group_info + student_list


if __name__ == "__main__":
    student1 = Student("Dima", 101)
    student2 = Student("Ivan", 102)

    group = Group("Class A")
    group.add_student(student1)
    group.add_student(student2)


print(group[0])
print(group[1])


for student in group:
    print(student)