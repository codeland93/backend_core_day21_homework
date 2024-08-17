import mysql.connector
from mysql.connector import Error

# Function to connect to the database
def connect_db():
    db_name = 'lm'
    user = 'root'
    password = 'juhki903'
    host = '127.0.0.1'

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print("Connection to MySQL database successful!")
            return conn

    except Error as e:
        print(f"Error: {e}")
        return None

# Class to manage library system operations
class LibraryManagementSystem:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    # Author management
    def author_add(self, name, biography=''):
        try:
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            self.cursor.execute(query, (name, biography))
            self.connection.commit()
            print("Author added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def author_fetch(self):
        try:
            query = "SELECT * FROM authors"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def author_update(self, author_id, name=None, biography=None):
        try:
            query = "UPDATE authors SET name = COALESCE(%s, name), biography = COALESCE(%s, biography) WHERE id = %s"
            self.cursor.execute(query, (name, biography, author_id))
            self.connection.commit()
            print("Author updated successfully!")
        except Error as e:
            print(f"Error: {e}")

    def author_delete(self, author_id):
        try:
            query = "DELETE FROM authors WHERE id = %s"
            self.cursor.execute(query, (author_id,))
            self.connection.commit()
            print("Author deleted successfully!")
        except Error as e:
            print(f"Error: {e}")

    # Book management
    def book_add(self, title, author_id, isbn, publication_date=None, availability=True):
        try:
            # Check if author exists
            self.cursor.execute("SELECT id FROM authors WHERE id = %s", (author_id,))
            if not self.cursor.fetchone():
                print("Error: Author ID does not exist.")
                return

            query = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (title, author_id, isbn, publication_date, availability))
            self.connection.commit()
            print("Book added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def book_fetch(self):
        try:
            query = "SELECT * FROM books"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def book_update(self, book_id, title=None, author_id=None, isbn=None, publication_date=None, availability=None):
        try:
            # Check if book exists
            self.cursor.execute("SELECT id FROM books WHERE id = %s", (book_id,))
            if not self.cursor.fetchone():
                print("Error: Book ID does not exist.")
                return

            # Check if author exists if author_id is provided
            if author_id is not None:
                self.cursor.execute("SELECT id FROM authors WHERE id = %s", (author_id,))
                if not self.cursor.fetchone():
                    print("Error: Author ID does not exist.")
                    return

            query = "UPDATE books SET title = COALESCE(%s, title), author_id = COALESCE(%s, author_id), isbn = COALESCE(%s, isbn), publication_date = COALESCE(%s, publication_date), availability = COALESCE(%s, availability) WHERE id = %s"
            self.cursor.execute(query, (title, author_id, isbn, publication_date, availability, book_id))
            self.connection.commit()
            print("Book updated successfully!")
        except Error as e:
            print(f"Error: {e}")

    def book_delete(self, book_id):
        try:
            query = "DELETE FROM books WHERE id = %s"
            self.cursor.execute(query, (book_id,))
            self.connection.commit()
            print("Book deleted successfully!")
        except Error as e:
            print(f"Error: {e}")

    # User management
    def user_add(self, name, library_id):
        try:
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            self.cursor.execute(query, (name, library_id))
            self.connection.commit()
            print("User added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def user_fetch(self):
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def user_update(self, user_id, name=None, library_id=None):
        try:
            query = "UPDATE users SET name = COALESCE(%s, name), library_id = COALESCE(%s, library_id) WHERE id = %s"
            self.cursor.execute(query, (name, library_id, user_id))
            self.connection.commit()
            print("User updated successfully!")
        except Error as e:
            print(f"Error: {e}")

    def user_delete(self, user_id):
        try:
            query = "DELETE FROM users WHERE id = %s"
            self.cursor.execute(query, (user_id,))
            self.connection.commit()
            print("User deleted successfully!")
        except Error as e:
            print(f"Error: {e}")

    # Borrowed books management
    def borrowed_books_add(self, user_id, book_id, borrow_date, return_date=None):
        try:
            # Check if user and book exist
            self.cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
            if not self.cursor.fetchone():
                print("Error: User ID does not exist.")
                return

            self.cursor.execute("SELECT id FROM books WHERE id = %s", (book_id,))
            if not self.cursor.fetchone():
                print("Error: Book ID does not exist.")
                return

            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (user_id, book_id, borrow_date, return_date))
            self.connection.commit()
            print("Borrowed book entry added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def borrowed_books_fetch(self):
        try:
            query = "SELECT * FROM borrowed_books"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def borrowed_books_update(self, id, user_id=None, book_id=None, borrow_date=None, return_date=None):
        try:
            # Check if borrowed book entry exists
            self.cursor.execute("SELECT id FROM borrowed_books WHERE id = %s", (id,))
            if not self.cursor.fetchone():
                print("Error: Borrowed book ID does not exist.")
                return

            # Check if user and book exist if user_id or book_id are provided
            if user_id is not None:
                self.cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
                if not self.cursor.fetchone():
                    print("Error: User ID does not exist.")
                    return

            if book_id is not None:
                self.cursor.execute("SELECT id FROM books WHERE id = %s", (book_id,))
                if not self.cursor.fetchone():
                    print("Error: Book ID does not exist.")
                    return

            query = "UPDATE borrowed_books SET user_id = COALESCE(%s, user_id), book_id = COALESCE(%s, book_id), borrow_date = COALESCE(%s, borrow_date), return_date = COALESCE(%s, return_date) WHERE id = %s"
            self.cursor.execute(query, (user_id, book_id, borrow_date, return_date, id))
            self.connection.commit()
            print("Borrowed book entry updated successfully!")
        except Error as e:
            print(f"Error: {e}")

    def borrowed_books_delete(self, id):
        try:
            query = "DELETE FROM borrowed_books WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()
            print("Borrowed book entry deleted successfully!")
        except Error as e:
            print(f"Error: {e}")

# Function to display the main menu and handle user input
def main_menu():
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database.")
        return

    lms = LibraryManagementSystem(conn)

    while True:
        print("\nWelcome to the Library Management System with Database Integration!")
        print("****")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("\nBook Operations:")
                print("1. Add a new book")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Search for a book")
                print("5. Display all books")
                print("6. Return to Main Menu")

                book_choice = input("Enter your choice: ")

                if book_choice == '1':
                    title = input("Enter the book title: ")
                    author_id = int(input("Enter the author ID: "))
                    isbn = input("Enter the ISBN: ")
                    publication_date = input("Enter the publication date (YYYY-MM-DD) or press Enter to skip: ")
                    publication_date = publication_date if publication_date else None
                    availability = input("Enter the availability (1 for available, 0 for not available): ")
                    availability = True if availability == '1' else False
                    lms.book_add(title, author_id, isbn, publication_date, availability)

                elif book_choice == '2':
                    user_id = int(input("Enter the user ID: "))
                    book_id = int(input("Enter the book ID: "))
                    borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")
                    lms.borrowed_books_add(user_id, book_id, borrow_date)

                elif book_choice == '3':
                    borrow_id = int(input("Enter the borrow record ID to update: "))
                    return_date = input("Enter the return date (YYYY-MM-DD) or press Enter to skip: ")
                    return_date = return_date if return_date else None
                    lms.borrowed_books_update(borrow_id, return_date=return_date)

                elif book_choice == '4':
                    search_term = input("Enter search term for the book (title or ISBN): ")
                    lms.book_fetch()  # Implement search functionality as needed

                elif book_choice == '5':
                    lms.book_fetch()

                elif book_choice == '6':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            while True:
                print("\nUser Operations:")
                print("1. Add a new user")
                print("2. View user details")
                print("3. Display all users")
                print("4. Return to Main Menu")

                user_choice = input("Enter your choice: ")

                if user_choice == '1':
                    name = input("Enter the user's name: ")
                    library_id = input("Enter the library ID: ")
                    lms.user_add(name, library_id)

                elif user_choice == '2':
                    user_id = int(input("Enter the user ID to view: "))
                    lms.user_fetch()  # Implement fetching specific user details as needed

                elif user_choice == '3':
                    lms.user_fetch()

                elif user_choice == '4':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            while True:
                print("\nAuthor Operations:")
                print("1. Add a new author")
                print("2. View author details")
                print("3. Display all authors")
                print("4. Return to Main Menu")

                author_choice = input("Enter your choice: ")

                if author_choice == '1':
                    name = input("Enter the author's name: ")
                    biography = input("Enter the author's biography: ")
                    lms.author_add(name, biography)

                elif author_choice == '2':
                    author_id = int(input("Enter the author ID to view: "))
                    lms.author_fetch()  # Implement fetching specific author details as needed

                elif author_choice == '3':
                    lms.author_fetch()

                elif author_choice == '4':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            conn.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
