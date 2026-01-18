import sqlite3

connection = sqlite3.connect("first_db.db")

cursor = connection.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT,
last_name TEXT
);
"""

cursor.execute(create_table_sql)

connection.commit()

insert_sql = """
INSERT INTO
    students (first_name, last_name)
VALUES
    ("Dean", "Jones"),
    ("Rowan", "Kavanagh")
;
"""

cursor.execute(insert_sql)

query_sql = """
SELECT *
FROM students
WHERE first_name IS 'Dean'
AND last_name IS 'Jones';
"""
dean_query = cursor.execute(query_sql).fetchall()




print(dean_query)

print(dean_query)


connection.commit()
connection.close()

