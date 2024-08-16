from db_connection import connect_db, Error

def fetch_all_customers():
    conn = connect_db()

    if conn is not None:
        try:

            cursor = conn.cursor() # messenger to travel back and forth using the connection we established

            # Select all from our customer table
            query = 'SELECT * FROM customer;'

            # Execute our query
            cursor.execute(query)

            for id, name, email, phone, addy in cursor.fetchall():
                print(f"{id}: {name}, {email}, {phone}, {addy}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close() # NEVER FORGET

def fetch_customer():
    conn = connect_db()

    if conn is not None:
        try:
            customer_id = input("What is the ID of the customer you're looking for? ")
            cursor = conn.cursor()

            query = "SELECT * FROM customer WHERE id = %s"

            cursor.execute(query, (customer_id,)) # any variables you include in your query need to be added as a tuple

            id, name, email, phone, addy = cursor.fetchone()
            # id, name, email, phone, addy = cursor.fetchall()[0] # also works, but fetchall() returns a list so we need to index into it to grab any values
            print(f"{id}: {name}, {email}, {phone}, {addy}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVVEEEERRRR FORGET!! O_O



if __name__ == "__main__":
#fetch_all_customers() 
   fetch_customer()           