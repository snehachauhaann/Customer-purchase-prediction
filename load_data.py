import sqlite3
import pandas as pd

def load_data():
    # Connect to database
    conn = sqlite3.connect("customer_data.db")

    # Retrieve data
    df = pd.read_sql_query("SELECT * FROM customers", conn)

    conn.close()

    return df

# Test the function
if __name__ == "__main__":
    data = load_data()
    print(data)
