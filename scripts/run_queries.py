import sqlite3

# Connect to your database
conn = sqlite3.connect("data/sql_db/trade.db")
cursor = conn.cursor()

# Example queries
queries = [
    "SELECT HS_CODE, SUM(VALUE) FROM trade_data GROUP BY HS_CODE LIMIT 5;",
    "SELECT PORT_CODE, COUNT(*) FROM trade_data GROUP BY PORT_CODE LIMIT 5;",
    "SELECT IEC, SUM(VALUE) FROM trade_data GROUP BY IEC LIMIT 5;",
    "SELECT ITEM_DESC, SUM(VALUE) FROM trade_data GROUP BY ITEM_DESC ORDER BY SUM(VALUE) DESC LIMIT 10;",
    "SELECT SUM(DUTY_PAID) FROM trade_data;"
]

# Run and print results
for q in queries:
    print(f"\nQuery: {q}")
    cursor.execute(q)
    for row in cursor.fetchall():
        print(row)

conn.close()