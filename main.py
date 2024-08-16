import os
from db_connection import connect_db, Error
from customer_add import add_customer
from customer_fetch import fetch_all_customers, fetch_customer
from author_add import add_author
from author_fetch import fetch_all_authors, fetch_author
from book_update import update_book
from user_update import update_user
from author_update import update_author

class LibraryManagementSystem:
    def __init__(self):
        self.db_connection = connect_db()
        if self.db_connection:
            self.cursor = self.db_connection.cursor()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        self.clear()
        while True:
            action = input('''
Welcome to the Library Management System with Database Integration!
****
Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Customer Menu                      
5. Quit
''')

            if action == '1':
                self.book_operations()
            elif action == '2':
                self.user_operations()
            elif action == '3':
                self.author_operations()
            elif action == '4':
                self.customer_menu()
            elif action == '5':
                if self.db_connection:
                    self.db_connection.close()
                break

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Update book details")
            print("7. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                self.update_book()
            elif choice == '7':
                break

    def verify_author_id(self, author_id):
        try:
            query = "SELECT author_id FROM authors WHERE author_id = %s"
            self.cursor.execute(query, (author_id,))
            result = self.cursor.fetchone()
            return result is not None
        except Error as e:
            print(f"Error: {e}")
            return False

    def add_book(self):
        title = input("Enter book title: ")
        author_id = input("Enter author ID: ")
        isbn = input("Enter ISBN number: ")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")

        if not self.verify_author_id(author_id):
            print("Error: The provided author ID does not exist.")
            return

        try:
            query = 'INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)'
            self.cursor.execute(query, (title, author_id, isbn, publication_date))
            self.db_connection.commit()
            print("Book added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def borrow_book(self):
        isbn = input("Enter ISBN number of the book to borrow: ")

        try:
            query = 'DELETE FROM books WHERE isbn = %s'
            self.cursor.execute(query, (isbn,))
            self.db_connection.commit()
            if self.cursor.rowcount > 0:
                print("Book borrowed successfully!")
            else:
                print("Book not found!")
        except Error as e:
            print(f"Error: {e}")

    def return_book(self):
        title = input("Enter book title: ")
        author_id = input("Enter author ID: ")
        isbn = input("Enter ISBN number: ")

        if not self.verify_author_id(author_id):
            print("Error: The provided author ID does not exist.")
            return

        try:
            query = 'INSERT INTO books (title, author_id, isbn) VALUES (%s, %s, %s)'
            self.cursor.execute(query, (title, author_id, isbn))
            self.db_connection.commit()
            print("Book returned successfully!")
        except Error as e:
            print(f"Error: {e}")

    def search_book(self):
        search_term = input("Enter book title or author: ")

        try:
            query = '''
                SELECT books.title, authors.name, books.isbn
                FROM books
                JOIN authors ON books.author_id = authors.author_id
                WHERE books.title LIKE %s OR authors.name LIKE %s
            '''
            self.cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
            results = self.cursor.fetchall()
            
            if results:
                for book in results:
                    print(f"Title: {book[0]}, Author: {book[1]}, ISBN: {book[2]}")
            else:
                print("No books found!")
        except Error as e:
            print(f"Error: {e}")

    def display_all_books(self):
        try:
            query = '''
                SELECT books.title, authors.name, books.isbn
                FROM books
                JOIN authors ON books.author_id = authors.author_id
            '''
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            if results:
                for book in results:
                    print(f"Title: {book[0]}, Author: {book[1]}, ISBN: {book[2]}")
            else:
                print("No books available!")
        except Error as e:
            print(f"Error: {e}")

    def update_book(self):
        update_book()

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Update user details")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                self.update_user()
            elif choice == '5':
                break

    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")

        try:
            query = 'INSERT INTO users (name, library_id) VALUES (%s, %s)'
            self.cursor.execute(query, (name, library_id))
            self.db_connection.commit()
            print("User added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def view_user_details(self):
        library_id = input("Enter library ID to view details: ")

        try:
            query = "SELECT * FROM users WHERE library_id = %s"
            self.cursor.execute(query, (library_id,))
            user = self.cursor.fetchone()
            
            if user:
                print(f"Name: {user[1]}, Library ID: {user[2]}")
            else:
                print("User not found!")
        except Error as e:
            print(f"Error: {e}")

    def display_all_users(self):
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            if results:
                for user in results:
                    print(f"Name: {user[1]}, Library ID: {user[2]}")
            else:
                print("No users available!")
        except Error as e:
            print(f"Error: {e}")

    def update_user(self):
        update_user()

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Update author details")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                self.update_author()
            elif choice == '5':
                break

    def add_author(self):
        name = input("Enter author name: ")
        birth_year = input("Enter birth year: ")

        try:
            query = 'INSERT INTO authors (name, birth_year) VALUES (%s, %s)'
            self.cursor.execute(query, (name, birth_year))
            self.db_connection.commit()
            print("Author added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def view_author_details(self):
        author_id = input("Enter author ID to view details: ")

        try:
            query = "SELECT * FROM authors WHERE author_id = %s"
            self.cursor.execute(query, (author_id,))
            author = self.cursor.fetchone()
            
            if author:
                print(f"Name: {author[1]}, Birth Year: {author[2]}, Author ID: {author[0]}")
            else:
                print("Author not found!")
        except Error as e:
            print(f"Error: {e}")

    def display_all_authors(self):
        try:
            query = "SELECT * FROM authors"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            if results:
                for author in results:
                    print(f"Name: {author[1]}, Birth Year: {author[2]}, Author ID: {author[0]}")
            else:
                print("No authors available!")
        except Error as e:
            print(f"Error: {e}")

    def update_author(self):
        update_author()

    def customer_menu(self):
        while True:
            print("\nCustomer Menu:")
            print("1. Add a customer")
            print("2. View customer details")
            print("3. Display all customers")
            print("4. Update customer details")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_customer()
            elif choice == '2':
                self.view_customer()
            elif choice == '3':
                self.display_all_customers()
            elif choice == '4':
                self.update_customer()
            elif choice == '5':
                break

    def add_customer(self):
        add_customer()

    def view_customer(self):
        fetch_customer()

    def display_all_customers(self):
        fetch_all_customers()

def update_customer(self):
    update_customer() 

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.main_menu()
