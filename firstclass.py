# EXP 1
# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor can't be zero")

#     return dividend / divisor


# def calculate(*values, operator):
#     return operator(*values)


# result = calculate(20, 4, operator=divide)
# print(result)

# EXP 2
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError("expected not found")


def get_friend_name(friend):
    return friend["name"]


friends = [
    {"name": "Rolfe Smith", "age": 23},
    {"name": "Bob Capta", "age": 25},
    {"name": "Jimmy Sodda", "age": 33}
]

print(search(friends, "Rolfe Smith", get_friend_name))
