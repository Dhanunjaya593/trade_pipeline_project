import pandas as pd
import sqlite3

# Step 1: Read the transformed CSV from Task 2
df = pd.read_csv("data/cleaned/transformed_data.csv")

# Step 2: Connect to SQLite database (it will create trade.db if not there)
conn = sqlite3.connect("data/sql_db/trade.db")

# Step 3: Save data into a table called trade_data
df.to_sql("trade_data", conn, if_exists="replace", index=False)

# Step 4: Close connection
conn.close()

print("Task 3 done. Data loaded into trade.db")