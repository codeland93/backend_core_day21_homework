from db_connection import connect_db, Error

def delete_customer():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            customer_id = input("What is the ID of the customer to delete? ")

            query = "SELECT customer_name FROM customer WHERE id = %s"
            cursor.execute(query, (customer_id,))
            name = cursor.fetchone()


            query = "DELETE FROM orders WHERE customer_id = %s"
            cursor.execute(query, (customer_id,))
            conn.commit()

            query = "DELETE FROM customer WHERE id = %s"
            cursor.execute(query, (customer_id,))
            conn.commit()

            print(f"Customer {name[0]} was successfully deleted!! Wow!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_customer()