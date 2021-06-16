class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f'{self.name} has grades {self.grades}'

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


studentA = Student("Bob", (90, 95, 88, 74, 98))
studentB = Student("Rolfe", (93, 45, 88, 70, 100))

print(studentA.name)
print(studentA.average_grade())

print(studentB.name)
print(studentB.average_grade())
