import sqlite3
import pandas as pd

# File paths
csv_file = "preprocessed_sales_data_sample.csv"  # Replace with your CSV file path
db_file = "sales_database.db"  # Desired SQLite database file

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file)

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect(db_file)

# Save DataFrame to SQLite (creates a table with the same name as the file, without extension)
table_name = "data"  # Name of the table to create
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print(f"Database created successfully with table '{table_name}' in file '{db_file}'.")
# Connect to the database
conn = sqlite3.connect("sales_database.db")
cursor = conn.cursor()

# Query the database
cursor.execute("SELECT * FROM data LIMIT 5;")
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close the connection
conn.close()


