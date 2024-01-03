import sqlite3
# ~~~~~~~~~~~~~~~~~~~~
# Connect to database
connect = sqlite3.connect('customer.db')
# ~~~~~~~~~~~~~~~~~~~~
# Creating a cursor
cursor = connect.cursor()
# ~~~~~~~~~~~~~~~~~~~~
# Create a table
# cursor.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
#     )
# """)
# ~~~~~~~~~~~~~~~~~~~~
# The five datatypes are:
# NULL (does, does not exist),
# INTEGER (whole number),
# REAL (decimal number),
# TEXT (text),
# BLOB (anything else, e.g., images, mp3)
# ~~~~~~~~~~~~~~~~~~~~
# INSERT A SINGLE TABLE ENTRY
# cursor.execute("INSERT INTO customers VALUES ('John','Elder','john@codemy.com')")
# ~~~~~~~~~~~~~~~~~~~~
# INSERT MULTIPLE TABLE ENTRIES AT ONCE
#
# many_customers = [
#     ('Dick', 'Grayson', 'dick@wayne.com'),
#     ('Damian', 'Wayne', 'damian@wayne.com'),
#     ('Bruce', 'Wayne', 'bruce@wayne.com'),
# ]
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
# ~~~~~~~~~~~~~~~~~~~~
# SELECTING ENTRIES FROM TABLE
# cursor.execute("SELECT * FROM customers")
# print(cursor.fetchone())
# print(cursor.fetchmany(3))
# all_items = cursor.fetchall()

# for item in all_items:
#     print(item[0]+" "+item[1]+", "+item[2])
# ~~~~~~~~~~~~~~~~~~~~
# ROW ID
# cursor.execute("SELECT rowid, * FROM customers")
# all_items = cursor.fetchall()
# for item in all_items:
#     print(item)
# ~~~~~~~~~~~~~~~~~~~~
# cursor.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
# all_items = cursor.fetchall()
# for item in all_items:
#     print(item)
# ~~~~~~~~~~~~~~~~~~~~
# UPDATING RECORDS
# cursor.execute("""UPDATE customers SET last_name = 'Stephanie'
#     WHERE last_name = 'Brown'
# """)
#
# cursor.execute("""UPDATE customers SET email = 'stephanie@wayne.com'
#      WHERE rowid = 1
# """)
# ~~~~~~~~~~~~~~~~~~~~
# DELETING RECORDS
# cursor.execute("DELETE FROM customers WHERE rowid >= 5")
# ~~~~~~~~~~~~~~~~~~~~
# ORDERING RESULTS
# cursor.execute("SELECT rowid, * FROM customers ORDER BY first_name DESC")
# all_items = cursor.fetchall()
# for item in all_items:
#     print(item)
# ~~~~~~~~~~~~~~~~~~~~
# AND/OR
# cursor.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Wa%' AND first_name LIKE 'B%'")
# all_items = cursor.fetchall()
# for item in all_items:
#     print(item)
# ~~~~~~~~~~~~~~~~~~~~
# LIMITING
# cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
# all_items = cursor.fetchall()
# for item in all_items:
#     print(item)
# ~~~~~~~~~~~~~~~~~~~~
# DELETE TABLE
# cursor.execute("DROP TABLE customers")
# ~~~~~~~~~~~~~~~~~~~~
# Commit our command
# connect.commit()

# Close our connection
# connect.close()
# ~~~~~~~~~~~~~~~~~~~~
# Query the database and return all records
def show_all():
    # Connect to database
    connect = sqlite3.connect('customer.db')

    # Create cursor
    cursor = connect.cursor()

    # Query the database
    cursor.execute("SELECT rowid, * FROM customers")
    all_items = cursor.fetchall()

    # Print each table item
    for item in all_items:
        print(item)

    # Close
    connect.close()
# ~~~~~~~~~~~~~~~~~~~~
# Add a new record to the table
def add_one(first=None, last=None, email=None):
    # Connect to database
    connect = sqlite3.connect('customer.db')

    # Create cursor
    cursor = connect.cursor()

    # Add a new entry
    cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first,last,email))

    # Commit changes
    connect.commit()

    # Close
    connect.close()
# ~~~~~~~~~~~~~~~~~~~~
