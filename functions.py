# student_attendance = {"Rolf": 96, "Bob": 77, "Karen": 55}

# for student, attendance in student_attendance.items():
#     print(f"{student} attended {attendance} classes")

def age():
    user_age = int(input("what is your age? "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")


age()
