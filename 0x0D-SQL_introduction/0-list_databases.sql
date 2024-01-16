import mysql.connector

# Replace these values with your MySQL server credentials
host = 'your_mysql_host'
user = 'your_mysql_user'
password = 'your_mysql_password'

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    # Create a cursor object to interact with the server
    cursor = connection.cursor()

    # Execute SQL query to retrieve the list of databases
    cursor.execute("SHOW DATABASES")

    # Fetch all the rows
    databases = cursor.fetchall()

    # Print the list of databases
    print("List of databases:")
    for db in databases:
        print(db[0])

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
