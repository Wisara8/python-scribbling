class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __repr__(self):
        return f"<Bookshelf with {len(self.books)} books>"


class Book:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Book {self.name}>"


book1 = Book("Harry Potter")
book2 = Book("Python 101")
book12 = Book("Pythonsssss Ahhhhh")


shelf = BookShelf(book1, book2, book12)

print(shelf)
