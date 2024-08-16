from db_connection import connect_db, Error

def update_user():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            # Get the ID of the user to update
            user_id = input("Enter the ID of the user you want to update: ")
            
            # Get new details from the user
            new_name = input("Enter the new name (leave blank to keep current): ")
            new_email = input("Enter the new email (leave blank to keep current): ")
            new_phone = input("Enter the new phone number (leave blank to keep current): ")
            new_address = input("Enter the new address (leave blank to keep current): ")

            # Prepare SQL update query
            query = "UPDATE users SET"
            updates = []
            parameters = []

            if new_name:
                updates.append("name = %s")
                parameters.append(new_name)
            if new_email:
                updates.append("email = %s")
                parameters.append(new_email)
            if new_phone:
                updates.append("phone = %s")
                parameters.append(new_phone)
            if new_address:
                updates.append("address = %s")
                parameters.append(new_address)
            
            # Ensure that we have at least one field to update
            if not updates:
                print("No fields to update. Exiting.")
                return
            
            query += " " + ", ".join(updates) + " WHERE id = %s"
            parameters.append(user_id)

            # Execute the update query
            cursor.execute(query, tuple(parameters))

            # Commit the changes
            conn.commit()
            print("User updated successfully!")

        except Error as e:
            print(f"Error: {e}")
            conn.rollback()  # Rollback in case of error

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    update_user()
