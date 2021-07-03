from database import add_entry, view_entries

# 3 commas for multi line commit
menu = """Please select one of the following: 
1) Add new entry for todat 
2)  View entries 
3) Exit 

Your Selection: """

welcome = "Welcome to the programming diary!"

# Walrus notation not available in insatlled version of Python

print(welcome)

user_input = input(menu)

while user_input != "3":
    # hadnle code here
    if user_input == "1":
        add_entry()
    elif user_input == "2":
        view_entries()
    else:
        print("Invalid option")

    user_input = input(menu)
