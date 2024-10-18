import sqlite3

def connect():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("bills.db")
    cursor = conn.cursor()
    # Create the bills table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_number TEXT,
            date TEXT,
            customer_name TEXT,
            amount REAL,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert(bill_number, date, customer_name, amount, status):
    # Insert a new bill into the database
    conn = sqlite3.connect("bills.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bills (bill_number, date, customer_name, amount, status) VALUES (?, ?, ?, ?, ?)",
                   (bill_number, date, customer_name, amount, status))
    conn.commit()
    conn.close()

def view():
    # Retrieve all bills from the database
    conn = sqlite3.connect("bills.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(bill_id):
    # Delete a bill from the database
    conn = sqlite3.connect("bills.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bills WHERE id=?", (bill_id,))
    conn.commit()
    conn.close()

def update(bill_id, bill_number, date, customer_name, amount, status):
    # Update a bill in the database
    conn = sqlite3.connect("bills.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE bills SET bill_number=?, date=?, customer_name=?, amount=?, status=? WHERE id=?",
                   (bill_number, date, customer_name, amount, status, bill_id))
    conn.commit()
    conn.close()
