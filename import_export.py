# DBMS Practical - Export & Import Data (MySQL + Python)
# -------------------------------------------------------
# Make sure to:
#   1. Install mysql-connector-python → pip install mysql-connector-python
#   2. Run MySQL as Administrator (so export/import file access works)
#   3. Adjust 'secure_file_priv' path if necessary

import mysql.connector

# MySQL connection setup
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hiddeN@123"   # Replace with your MySQL password
)

cur = con.cursor()

# Step 1. Create Database
cur.execute("CREATE DATABASE IF NOT EXISTS export_import_data;")
cur.execute("USE export_import_data;")

# Step 2. Create Main Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        emp_id INT PRIMARY KEY,
        emp_name VARCHAR(50),
        salary INT
    );
""")

# Step 3. Insert Sample Records
cur.execute("DELETE FROM Employee;")  # clear old data
cur.executemany(
    "INSERT INTO Employee (emp_id, emp_name, salary) VALUES (%s, %s, %s);",
    [
        (1, 'Advay', 50000),
        (2, 'Manisha', 45000),
        (3, 'Om', 30000)
    ]
)
con.commit()
print("Sample data inserted into Employee table.\n")

# Step 4. Check allowed export path
cur.execute("SHOW VARIABLES LIKE 'secure_file_priv';")
export_path = cur.fetchone()[1]
print(f"MySQL secure file path: {export_path}")

# Define CSV file path (must be inside secure_file_priv folder)
csv_file = export_path.rstrip("\\/") + "/employee.csv"

# Step 5. Export data to CSV file
export_query = f"""
SELECT emp_id, emp_name, salary
INTO OUTFILE '{csv_file}'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\\n'
FROM Employee;
"""
try:
    cur.execute(export_query)
    print(f"Data exported successfully to:\n   {csv_file}\n")
except mysql.connector.Error as e:
    print(f"Export failed: {e}\n")

# Step 6. Create copy table for import
cur.execute("""
    CREATE TABLE IF NOT EXISTS Employee_copy (
        emp_id INT PRIMARY KEY,
        emp_name VARCHAR(50),
        salary INT
    );
""")
cur.execute("DELETE FROM Employee_copy;")
con.commit()

# Step 7. Import data from CSV file
import_query = f"""
LOAD DATA INFILE '{csv_file}'
INTO TABLE Employee_copy
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\\n';
"""
try:
    cur.execute(import_query)
    con.commit()
    print("Data imported successfully into Employee_copy.\n")
except mysql.connector.Error as e:
    print(f"Import failed: {e}\n")

# Step 8. Display imported data
cur.execute("SELECT * FROM Employee_copy;")
rows = cur.fetchall()

print("Employee_copy table contents:")
for row in rows:
    print(row)

# Step 9. Close connection
con.close()
print("\nMySQL connection closed successfully.")
