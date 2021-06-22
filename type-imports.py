from errorExp import divide

print("welcome to divisor programe")

grades = []
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("no grades yet")

print(f"average grade is {average}")
