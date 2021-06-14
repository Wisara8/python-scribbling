class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f'{self.name} has grades {self.grades}'

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (90, 95, 88, 74, 98))
print(student)
print(student.name)
print(student.average_grade())
