# Import necessary library for file handling
import json

# Initialize library as an empty list to store book details
library = []

# Function to add a new book to the library
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    # Convert user input to boolean for read status
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    # Create a dictionary for the new book
    book = {"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status}
    # Append the new book to the library list
    library.append(book)
    print("Book added successfully!")

# Function to remove a book by its title
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():  # Match title case-insensitively
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Function to search for books by title or author
def search_books():
    choice = input("Search by: \n1. Title \n2. Author \nEnter your choice: ").strip()
    query = input("Enter your search query: ").strip().lower()
    # Filter the library based on user's query
    results = [book for book in library if query in book[("title" if choice == "1" else "author")].lower()]
    if results:
        print("Matching Books:")
        for book in results:
            print(format_book(book))
    else:
        print("No matching books found!")

# Function to display all books in the library
def display_books():
    if library:
        print("Your Library:")
        for book in library:
            print(format_book(book))
    else:
        print("No books in the library!")

# Function to display total books and read percentage
def display_statistics():
    total_books = len(library)
    read_books = sum(book["read_status"] for book in library)
    # Calculate and display statistics
    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_books / total_books * 100:.2f}%" if total_books > 0 else "No books to calculate statistics.")

# Function to save the library to a file on exit
def save_library_to_file():
    with open("library.txt", "w") as file:
        json.dump(library, file)
    print("Library saved to file.")

# Function to load the library from a file on startup
def load_library_from_file():
    try:
        with open("library.txt", "r") as file:
            global library
            library = json.load(file)
    except FileNotFoundError:
        pass  # Ignore error if file doesn't exist

# Helper function to format book details for display
def format_book(book):
    return f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {"Read" if book["read_status"] else "Unread"}'

# Main program logic with menu system
def main():
    load_library_from_file()  # Load library data from file at startup
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library_to_file()  # Save library data to file on exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Start the program
if __name__ == "__main__":
    main()
