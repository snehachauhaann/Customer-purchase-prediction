import sqlite3

def create_database():
    conn = sqlite3.connect("customer_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        salary INTEGER,
        purchased INTEGER
    )
    """)

    conn.commit()
    conn.close()

    print("Database and table created successfully!")
create_database()