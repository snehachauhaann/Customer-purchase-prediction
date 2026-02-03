import sqlite3

def insert_sample_data():
    conn = sqlite3.connect("customer_data.db")
    cursor = conn.cursor()

    data = [
        (25, 50000, 0),
        (35, 65000, 1),
        (45, 80000, 1),
        (23, 48000, 0),
        (40, 72000, 1),
        (30, 54000, 0),
        (50, 90000, 1),
        (28, 52000, 0)
    ]

    cursor.executemany(
        "INSERT INTO customers(age, salary, purchased) VALUES (?, ?, ?)",
        data
    )

    conn.commit()
    conn.close()

    print("Sample data inserted successfully!")

insert_sample_data()
