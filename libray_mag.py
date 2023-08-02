class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("List of books in the library:")
            for book in self.books:
                print(f"{book.title} by {book.author}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book '{book.title}' by {book.author} found.")
                return
        print(f"Book with title '{title}' not found in the library.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice (1 or 2 or 3 or 4): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.add_book(title, author)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter the title of the book you want to search: ")
            library.search_book(title)

        elif choice == '4':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()