class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, type {self.type}, weighs {self.weight}g>"


book = Book("Harry Potter", "hardcover", 1500)

print(book)
print(book.name)
