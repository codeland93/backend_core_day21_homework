import mysql.connector
from mysql.connector import Error

# Function to connect to the database
def connect_db():
    db_name = 'lms'
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

    # Borrowed books management (Placeholder method)
    def borrowed_books(self):
        try:
            query = "SELECT * FROM borrowed_books"  # Example query, adjust based on your schema
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    # Customer management
    def customer_add(self, name, email):
        try:
            query = "INSERT INTO customers (name, email) VALUES (%s, %s)"
            self.cursor.execute(query, (name, email))
            self.connection.commit()
            print("Customer added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def customer_delete(self, customer_id):
        try:
            query = "DELETE FROM customers WHERE id = %s"
            self.cursor.execute(query, (customer_id,))
            self.connection.commit()
            print("Customer deleted successfully!")
        except Error as e:
            print(f"Error: {e}")

    def customer_fetch(self):
        try:
            query = "SELECT * FROM customers"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")

    def customer_update(self, customer_id, name=None, email=None):
        try:
            query = "UPDATE customers SET name = %s, email = %s WHERE id = %s"
            self.cursor.execute(query, (name, email, customer_id))
            self.connection.commit()
            print("Customer updated successfully!")
        except Error as e:
            print(f"Error: {e}")

    def user_update(self, user_id, username=None, password=None):
        try:
            query = "UPDATE users SET username = %s, password = %s WHERE id = %s"
            self.cursor.execute(query, (username, password, user_id))
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
    library_system.customer_add("John Doe", "john.doe@example.com")
    # Add more method calls as needed
else:
    print("Failed to connect to the database.")
