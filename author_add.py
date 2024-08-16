from db_connection import connect_db, Error

def add_author():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("what is the name of the book? ").title()
            email = input("What is the author email? ")
            phone = input("what is the author phone number? ")

            new_customer = (name, email, phone)

            query = "INSERT INTO customer (author_name, email, phone) VALUES (%s, %s, %s)"

            cursor.execute(query, new_customer)
            conn.commit() # fully commits the changes that we're trying to make (addingdata to teh customer table)
            print(f"New author {name} added successfully!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close() # ALWAYS
                
if __name__ == "__main__":
  add_author()