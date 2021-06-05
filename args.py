def multiply(*args):
    # print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

# def add(x, y):
#     total = x + y
#     return total


# num = {'x': 5, 'y': 3}
# print(add(**num))

def apply(*args, operator):
    if operator == '+':
        return sum(args)
    elif operator == '*':
        # print("apply")
        return multiply(*args)
    else:
        return "Not computed"


print(apply(1, 3, 5, operator='*'))
