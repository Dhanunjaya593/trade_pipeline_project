import sqlite3

# Connect to your database
conn = sqlite3.connect("data/sql_db/trade.db")
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in trade.db:", cursor.fetchall())

# Show columns for trade_data table
print("\nColumns in trade_data:")
cursor.execute("PRAGMA table_info(trade_data);")
for row in cursor.fetchall():
    print(row)

conn.close()