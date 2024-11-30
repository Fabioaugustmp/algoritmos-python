class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} {'(Borrowed)' if self.is_borrowed else ''}"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} successfully returned {book.title}.")
        else:
            print(f"{self.name} cannot return {book.title} as it was not borrowed by them.")

    def __str__(self):
        borrowed = ', '.join([book.title for book in self.borrowed_books]) or "No books"
        return f"Member: {self.name}, Borrowed books: {borrowed}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def list_books(self):
        print(f"\nBooks available in {self.name}:")
        for book in self.books:
            print(book)

    def __str__(self):
        return f"Library: {self.name}, Total books: {len(self.books)}"


# Example usage
library = Library("Central Library")
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member = Member("Alice")
library.list_books()

member.borrow_book(book1)
member.borrow_book(book2)
library.list_books()

member.return_book(book1)
library.list_books()
print(member)

