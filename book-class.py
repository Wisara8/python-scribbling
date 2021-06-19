class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, type {self.type}, weighs {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
book_light = Book.paperback("Python 101", 900)


print(book)
print(book_light)
