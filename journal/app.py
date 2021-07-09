from database import create_table, add_entry, get_entries

# 3 commas for multi line commit
menu = """Please select one of the following: 
1) Add new entry for today 
2) View entries 
3) Exit 

Your Selection: """

welcome = "Welcome to the programming diary!"


def prompt_new_entry():
    entry_content = input("What did we learn today? ")
    entry_date = input("enter the date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


print(welcome)
create_table()

user_input = input(menu)

while user_input != "3":
    # hadnle code here
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())

    else:
        print("Invalid option")

    user_input = input(menu)
