import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("data/sql_db/trade.db")

# --- HS CODE Totals ---
hs_query = 'SELECT "HS CODE", SUM("TOTAL VALUE_INR") as total_value FROM trade_data GROUP BY "HS CODE";'
hs_df = pd.read_sql_query(hs_query, conn)
hs_df.plot(kind="bar", x="HS CODE", y="total_value", legend=False)
plt.title("HS Code Totals (INR)")
plt.xlabel("HS Code")
plt.ylabel("Total Value (INR)")
plt.tight_layout()
plt.show()

# --- PORT CODE Counts ---
port_query = 'SELECT "PORT CODE", COUNT(*) as shipment_count FROM trade_data GROUP BY "PORT CODE";'
port_df = pd.read_sql_query(port_query, conn)
port_df.plot(kind="bar", x="PORT CODE", y="shipment_count", legend=False)
plt.title("Port Code Shipment Counts")
plt.xlabel("Port Code")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# --- IEC Totals ---
iec_query = 'SELECT IEC, SUM("TOTAL VALUE_INR") as total_value FROM trade_data GROUP BY IEC;'
iec_df = pd.read_sql_query(iec_query, conn)
iec_df.plot(kind="bar", x="IEC", y="total_value", legend=False)
plt.title("IEC Totals (INR)")
plt.xlabel("IEC")
plt.ylabel("Total Value (INR)")
plt.tight_layout()
plt.show()

# --- Top 10 Goods ---
item_query = '''
SELECT "GOODS DESCRIPTION", SUM("TOTAL VALUE_INR") as total_value
FROM trade_data
GROUP BY "GOODS DESCRIPTION"
ORDER BY total_value DESC
LIMIT 10;
'''
item_df = pd.read_sql_query(item_query, conn)
item_df.plot(kind="bar", x="GOODS DESCRIPTION", y="total_value", legend=False)
plt.title("Top 10 Goods by Value (INR)")
plt.xlabel("Goods Description")
plt.ylabel("Total Value (INR)")
plt.tight_layout()
plt.show()

# --- Duty Paid Summary ---
duty_query = 'SELECT SUM("DUTY PAID_INR") as total_duty FROM trade_data;'
duty_df = pd.read_sql_query(duty_query, conn)
print("Total Duty Paid (INR):", duty_df["total_duty"].iloc[0])

# --- Year-wise Breakdown ---
year_query = '''
SELECT SUBSTR(DATE, 1, 4) as Year, SUM("TOTAL VALUE_INR") as total_value
FROM trade_data
GROUP BY Year
ORDER BY Year;
'''
year_df = pd.read_sql_query(year_query, conn)
year_df.plot(kind="line", x="Year", y="total_value", marker="o")
plt.title("Year-wise Trade Value (INR)")
plt.xlabel("Year")
plt.ylabel("Total Value (INR)")
plt.tight_layout()
plt.show()

conn.close()