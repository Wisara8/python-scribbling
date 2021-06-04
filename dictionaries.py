users = [
    (0, "Bob", "password"),
    (1, "Rolfe", "Rolfe123"),
    (2, "Jose", "Noway"),
    (3, "Jose", "Noway")

]

username_mapping = {user[1]: user for user in users}

print(username_mapping)

username_input = input("enter username: ")
userpassword_input = input("enter password: ")

_, username, password = username_mapping[username_input]

if password == userpassword_input:
    print("correct")
else:
    print("wrong")
