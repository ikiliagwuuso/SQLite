import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")

# Create a cursor
c = conn.cursor()

# Create a Student Table
#c.execute("INSERT INTO students VALUES('George', 'Igwegbe', 'gigewgbe@gmail.com', 'DataScience')")
c.execute("INSERT INTO students VALUES('Cyroma', 'George', 'cyroma.george@gmail.com', 'DataScience')")

print("Command executed successfully...")

# Commit our command
conn.commit()

# Close our connection
conn.close()
