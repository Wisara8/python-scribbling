entries = []


def add_entry():
    entry_content = input("What did we learn today? ")
    entry_date = input("enter the date: ")

    entries.append({"content": entry_content, "date": entry_date})


def view_entries():
    pass
