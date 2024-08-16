from db_connection import connect_db, Error

def update_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            # Get the ID of the book to update
            book_id = input("Enter the ID of the book you want to update: ")
            
            # Get new details from the user
            new_title = input("Enter the new title (leave blank to keep current): ")
            new_author = input("Enter the new author (leave blank to keep current): ")
            new_isbn = input("Enter the new ISBN number (leave blank to keep current): ")

            # Prepare SQL update query
            query = "UPDATE books SET"
            updates = []
            parameters = []

            if new_title:
                updates.append("title = %s")
                parameters.append(new_title)
            if new_author:
                updates.append("author = %s")
                parameters.append(new_author)
            if new_isbn:
                updates.append("isbn = %s")
                parameters.append(new_isbn)
            
            # Ensure that we have at least one field to update
            if not updates:
                print("No fields to update. Exiting.")
                return
            
            query += " " + ", ".join(updates) + " WHERE id = %s"
            parameters.append(book_id)

            # Execute the update query
            cursor.execute(query, tuple(parameters))

            # Commit the changes
            conn.commit()
            print("Book updated successfully!")

        except Error as e:
            print(f"Error: {e}")
            conn.rollback()  # Rollback in case of error

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    update_book()
