from book import Book
from library import Library


def main():
    book1 = Book("cats", "author1")
    book2 = Book("clouds", "author2")
    book3 = Book("cats 2", "author1")
    book4 = Book("rabbits", "author3")

    library = Library()
    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))
    print(library.add_book(book4))

    print(library)
    print(library.search_by_author("auth"))
    print(library.search_by_author("author1"))
    print(library.search_by_author("author2"))

    print(library.search_by_title("cats"))
    print(library.search_by_title("clouds"))
    print(library.search_by_title("rabbit"))

    print(library.fuzzy_search_by_author("auth"))
    print(library.fuzzy_search_by_title("cats"))


if __name__ == "__main__":
    main()
