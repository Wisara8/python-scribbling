from errorExp import divide

print("welcome to divisor programe")

grades = []
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("no grades yet")
else:
    print(f"average grade is {average}")
finally:
    print("I always run regardless")
