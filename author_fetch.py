from db_connection import connect_db, Error

def fetch_all_authors():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM authors;'
            cursor.execute(query)
            
            for author in cursor.fetchall():
                author_id, name, birth_year, biography = author
                print(f"ID: {author_id}, Name: {name}, Birth Year: {birth_year}, Biography: {biography}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def fetch_author():
    conn = connect_db()

    if conn is not None:
        try:
            author_id = input("Enter the ID of the author you're looking for: ")
            cursor = conn.cursor()
            query = "SELECT * FROM authors WHERE author_id = %s"
            cursor.execute(query, (author_id,))

            author = cursor.fetchone()
            if author:
                author_id, name, birth_year, biography = author
                print(f"ID: {author_id}, Name: {name}, Birth Year: {birth_year}, Biography: {biography}")
            else:
                print("Author not found!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
