student = {'name': "Bob", "grades": (80, 90, 97, 95, 84)}


def average(grades):
    return sum(grades) / len(grades)


print(average(student['grades']))
