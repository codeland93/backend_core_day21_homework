from db_connection import connect_db, Error

def fetch_all_borrowed_books():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            # Select all from the borrowed_books table
            query = 'SELECT * FROM borrowed_books;'

            cursor.execute(query)

            for id, user_id, book_id, borrow_date, return_date in cursor.fetchall():
                print(f"ID: {id}, User ID: {user_id}, Book ID: {book_id}, Borrow Date: {borrow_date}, Return Date: {return_date}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def fetch_borrowed_book():
    conn = connect_db()

    if conn is not None:
        try:
            borrowed_id = input("Enter the ID of the borrowed book record you're looking for: ")
            cursor = conn.cursor()

            query = "SELECT * FROM borrowed_books WHERE id = %s"

            cursor.execute(query, (borrowed_id,)) 

            result = cursor.fetchone()
            if result:
                id, user_id, book_id, borrow_date, return_date = result
                print(f"ID: {id}, User ID: {user_id}, Book ID: {book_id}, Borrow Date: {borrow_date}, Return Date: {return_date}")
            else:
                print("No borrowed book record found with that ID.")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_all_borrowed_books()
    fetch_borrowed_book()
