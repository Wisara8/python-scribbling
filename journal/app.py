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
        print("adding...")
    elif user_input == "2":
        print("Viewing")
    else:
        print("Invalid option")

    user_input = input(menu)
