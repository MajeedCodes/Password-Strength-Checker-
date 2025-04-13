class LibraryManager:
    def __init__(self):
        self.library = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        while True:

            try:
                year = int(input("Enter publication year: "))
                break
            except ValueError:
                print("Please enter a valid year (number)")
        genre = input("Enter genre: ")
        while True:
            read = input("Have you read this book? (yes/no): ").lower()
            if read in ['yes', 'no']:
                read_status = True if read == 'yes' else False
                break
            print("Please enter 'yes' or 'no'")
        
        book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read_status
        }
        self.library.append(book)
        print(f"'{title}' has been added to the library.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for i, book in enumerate(self.library):
            if book['title'].lower() == title.lower():
                del self.library[i]
                print(f"'{title}' has been removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def search_book(self):
        search_term = input("Enter title or author to search: ").lower()
        matches = [book for book in self.library if 
                  search_term in book['title'].lower() or 
                  search_term in book['author'].lower()]
        
        if matches:
            print("\nMatching books:")
            self.display_books(matches)
        else:
            print("No matches found.")

    def display_books(self, books):
        for book in books:
            read_status = "Read" if book['read'] else "Unread"
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Status: {read_status}")
            print("-" * 30)

    def display_stats(self):
        total_books = len(self.library)
        if total_books == 0:
            print("Library is empty.")
            return
        
        read_books = sum(1 for book in self.library if book['read'])
        percentage = (read_books / total_books) * 100 if total_books > 0 else 0
        
        print(f"Total books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Percentage read: {percentage:.2f}%")

def main():
    library = LibraryManager()
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.remove_book()
        elif choice == '3':
            library.search_book()
        elif choice == '4':
            if library.library:
                library.display_books(library.library)
            else:
                print("Library is empty.")
        elif choice == '5':
            library.display_stats()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
