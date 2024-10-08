
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
    def author_add(self, name):
        try:
            query = "INSERT INTO authors (name) VALUES (%s)"
            self.cursor.execute(query, (name,))
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

    def author_update(self, author_id, name):
        try:
            query = "UPDATE authors SET name = %s WHERE id = %s"
            self.cursor.execute(query, (name, author_id))
            self.connection.commit()
            print("Author updated successfully!")
        except Error as e:
            print(f"Error: {e}")

    # Book management
    def book_fetch(self):
        try:
            query = "SELECT * FROM books"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def book_update(self, book_id, title=None, author_id=None, isbn=None):
        try:
            query = "UPDATE books SET title = %s, author_id = %s, isbn = %s WHERE id = %s"
            self.cursor.execute(query, (title, author_id, isbn, book_id))
            self.connection.commit()
            print("Book updated successfully!")
        except Error as e:
            print(f"Error: {e}")

    # Borrowed books management
    def borrowed_books(self):
        try:
            query = "SELECT * FROM borrowed_books"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
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
            query = "UPDATE users SET name = %s, library_id = %s WHERE id = %s"
            self.cursor.execute(query, (name, library_id, user_id))
            self.connection.commit()
            print("User updated successfully!")
        except Error as e:
            print(f"Error: {e}")

# Main execution
db_connection = connect_db()
if db_connection:
    library_system = LibraryManagementSystem(db_connection)
    # Example usage of methods
    library_system.author_add("J.K. Rowling")
    library_system.book_fetch()
    library_system.user_add("John Doe", "1234567890")
    # Add more method calls as needed
else:
    print("Failed to connect to the database.")
