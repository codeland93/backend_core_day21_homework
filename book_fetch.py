from db_connection import connect_db, Error

def fetch_all_books():
    conn = connect_db()

    if conn is not None:
        try:

            cursor = conn.cursor()

           
            query = 'SELECT * FROM book;'

           
            cursor.execute(query)

            for id, name, email, phone, addy in cursor.fetchall():
                print(f"{id}: {name}, {email}, {phone}, {addy}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close() 

def fetch_book():
    conn = connect_db()

    if conn is not None:
        try:
            book_id = input("What is the ID of the book you're looking for? ")
            cursor = conn.cursor()

            query = "SELECT * FROM book WHERE id = %s"

            cursor.execute(query, (book_id,)) 

            id, name, genre = cursor.fetchone()
            print(f"{id}: {name}, {genre}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() 


if __name__ == "__main__":
   fetch_all_books()
   fetch_book()           