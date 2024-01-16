import mysql.connector
import sys

# Replace these values with your MySQL server credentials
host = 'your_mysql_host'
user = 'your_mysql_user'
password = 'your_mysql_password'

def list_tables(database):
    try:
        # Connect to MySQL server with specified database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to interact with the server
        cursor = connection.cursor()

        # Execute SQL query to retrieve the list of tables
        cursor.execute("SHOW TABLES")

        # Fetch all the rows
        tables = cursor.fetchall()

        # Print the list of tables
        print(f"List of tables in database '{database}':")
        for table in tables:
            print(table[0])

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_tables.py <database_name>")
        sys.exit(1)

    database_name = sys.argv[1]
    list_tables(database_name)

