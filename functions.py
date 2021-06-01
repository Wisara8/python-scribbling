# student_attendance = {"Rolf": 96, "Bob": 77, "Karen": 55}

# for student, attendance in student_attendance.items():
#     print(f"{student} attended {attendance} classes")

# def age():
#     user_age = int(input("what is your age? "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}")


# age()

# def sum(x, y):
#     return x + y


# result = sum(5, y=8)
# # note you can't do the opposite of defining x and not y; if the first is declared the rest must be too
# print(result)

def double(x):
    return x * 2


sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]
# does the same as below
doubledWithMap = map(double, sequence)
# and this
doubledWithLamba = map(lambda x: x * 2, sequence)
# with the lamba you won't need the double(x) function
