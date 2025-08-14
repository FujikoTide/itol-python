from dataclasses import dataclass, field
from _types import books
from book import Book


@dataclass
class Library:
    books: "books" = field(default_factory=dict)

    def add_book(self, book: Book) -> Book | None:
        if not isinstance(book, Book):
            return None
        if book.ISBN not in self.books:
            self.books[book.ISBN] = (book, 1)
            return book
        self.books[book.ISBN] = (book, self.books[book.ISBN][1] + 1)
        return book

    def lend_book(self, book_isbn: str) -> Book | None:
        if not isinstance(book_isbn, str):
            return None
        if book_isbn not in self.books:
            return None
        book, quantity = self.books[book_isbn]
        if quantity > 0:
            self.books[book_isbn] = (book, quantity - 1)
            return book
        return None

    def search_by_author(self, author: str) -> list[Book] | None:
        if not isinstance(author, str):
            return None
        return [book for book, _ in self.books.values() if author == book.author]

    def search_by_title(self, title: str) -> list[Book] | None:
        if not isinstance(title, str):
            return None
        return [book for book, _ in self.books.values() if title == book.title]

    def fuzzy_search_by_author(self, author: str) -> list[Book] | None:
        if not isinstance(author, str):
            return None
        return [book for book, _ in self.books.values() if author in book.author]

    def fuzzy_search_by_title(self, title: str) -> list[Book] | None:
        if not isinstance(title, str):
            return None
        return [book for book, _ in self.books.values() if title in book.title]
