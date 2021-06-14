class Student:
    def __init__(self):
        self.name = "Rolfe"
        self.grades = (90, 95, 88, 74, 98)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()

print(student.average_grade())
