import sqlite3

conn = sqlite3.connect('customer.db')
# cursor
c = conn.cursor()


# create a table
# c.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
# )
# """)

# c.execute("INSERT INTO customers VALUES ('Ahmed','JAmadar','Ahmed@gmail.com')")
c.execute("SELECT * FROM customers")

print(c.fetchall())
conn.commit()
conn.close()

print('Musheer is the best coder in the world')
# NULL,INTEGER,REAL,TEXT,BLOB
