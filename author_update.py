from db_connection import connect_db, Error

def update_author():
    author_id = input("Enter the Author ID of the author you want to update: ").strip()

    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Fetch current details
            cursor.execute("SELECT * FROM authors WHERE author_id = %s", (author_id,))
            author = cursor.fetchone()
            
            if author:
                print(f"Current Name: {author[1]}")
                new_name = input("Enter new name (leave blank to keep current): ").strip() or author[1]
                
                print(f"Current Birth Year: {author[2]}")
                new_birth_year_input = input("Enter new birth year (leave blank to keep current): ").strip()
                # Ensure that birth year is an integer or keep the current value
                new_birth_year = int(new_birth_year_input) if new_birth_year_input else author[2]

                query = "UPDATE authors SET name = %s, birth_year = %s WHERE author_id = %s"
                cursor.execute(query, (new_name, new_birth_year, author_id))
                conn.commit()

                if cursor.rowcount > 0:
                    print("Author updated successfully!")
                else:
                    print("No changes were made.")
            else:
                print("Author not found!")

        except Error as e:
            print(f"Error: {e}")
        except ValueError as ve:
            print(f"Value Error: {ve}")
        finally:
            cursor.close()
            conn.close()
