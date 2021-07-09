import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES ('This is test content', '2021-01-01');"
        )


def get_entries():
    return entries
