class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}"

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

class Bookshelf:
    books = []

    def __init__(self, capacity):
        self.capacity = capacity

    def listAllBooks(self):
        for book in self.books:
            print(f"Book on the shelf: {book.__str__()}")

    def addBook(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
            return f"{book.getTitle()} added to the book shelf."
        else:
            return f"{book.getTitle()} not added, shelf is full."

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book.getTitle()} has been removed from the shelf.")
        else:
            print(f"{book.getTitle()} is not on the shelf, thus, it has not been removed.")

    def findTitle(self, title):
        for book in self.books:
            if book.getTitle() == title:
                print(f"{title} found!")
                return (book)
            else:
                return f"{title} is not on the book shelf"

    def findAuthor(self, author):
        authorsBooks = []
        for book in self.books:
            if author == book.getAuthor():
                authorsBooks.append(book.__str__())
        return authorsBooks


book1 = Book("Shining", "King", "Penguin", 1980)
book2 = Book("Harry Potter", "Peter", "Penguin", 2000)
book3 = Book("Sci fi book", "Peter", "British London", 1950)
book4 = Book("Horror", "Jim", "American", 1800)

bookshelf1 = Bookshelf(3)

print(bookshelf1.addBook(book1))
print(bookshelf1.addBook(book2))
print(bookshelf1.addBook(book3))
print(bookshelf1.addBook(book4))
bookshelf1.listAllBooks()
bookshelf1.removeBook(book1)
print(bookshelf1.findTitle(book1.getTitle()))
print(bookshelf1.findTitle(book2.getTitle()))
print(bookshelf1.findAuthor("Peter"))