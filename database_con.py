# DBMS Practical 6 - Python MySQL Connection

import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hiddeN@123",   # Replace with your actual password
    database="practical6"
)

cur = con.cursor()

# Insert record into 'student' table
cur.execute("INSERT INTO student VALUES (3, 'Ravi', 90)")
con.commit()
print("✅ Record inserted successfully!")

# Retrieve data from 'student' table
cur.execute("SELECT * FROM student;")

print("\n📘 Student Table Data:")
for row in cur.fetchall():
    print(row)

# Close connection
con.close()
print("\n🔒 Connection closed.")
