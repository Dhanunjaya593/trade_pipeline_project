import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

# Connect to database
@st.cache_data
def load_data():
    conn = sqlite3.connect("data/sql_db/trade.db")
    df = pd.read_sql_query("SELECT * FROM trade_data;", conn)
    conn.close()
    return df

df = load_data()

st.title("📊 Trade Dashboard")

# --- Filters ---
years = sorted(df["DATE"].str[:4].unique())
hs_codes = sorted(df["HS CODE"].unique())
ports = sorted(df["PORT CODE"].unique())

year_filter = st.multiselect("Select Year(s)", years, default=years)
hs_filter = st.multiselect("Select HS Code(s)", hs_codes)
port_filter = st.multiselect("Select Port(s)", ports)

filtered_df = df.copy()
if year_filter:
    filtered_df = filtered_df[filtered_df["DATE"].str[:4].isin(year_filter)]
if hs_filter:
    filtered_df = filtered_df[filtered_df["HS CODE"].isin(hs_filter)]
if port_filter:
    filtered_df = filtered_df[filtered_df["PORT CODE"].isin(port_filter)]

# --- Charts ---
st.subheader("Year-wise Trade Value (INR)")
year_summary = (
    filtered_df.groupby(filtered_df["DATE"].str[:4])["TOTAL VALUE_INR"].sum().reset_index()
)
fig_year = px.line(year_summary, x="DATE", y="TOTAL VALUE_INR", markers=True)
st.plotly_chart(fig_year)

st.subheader("HS Code Totals (INR)")
hs_summary = filtered_df.groupby("HS CODE")["TOTAL VALUE_INR"].sum().reset_index()
fig_hs = px.bar(hs_summary, x="HS CODE", y="TOTAL VALUE_INR")
st.plotly_chart(fig_hs)

st.subheader("Port Code Shipment Counts")
port_summary = filtered_df.groupby("PORT CODE").size().reset_index(name="shipment_count")
fig_port = px.bar(port_summary, x="PORT CODE", y="shipment_count")
st.plotly_chart(fig_port)

st.subheader("Top 10 Goods by Value (INR)")
goods_summary = (
    filtered_df.groupby("GOODS DESCRIPTION")["TOTAL VALUE_INR"].sum()
    .reset_index()
    .sort_values("TOTAL VALUE_INR", ascending=False)
    .head(10)
)
fig_goods = px.bar(goods_summary, x="GOODS DESCRIPTION", y="TOTAL VALUE_INR")
st.plotly_chart(fig_goods)

st.subheader("Duty Paid Summary")
total_duty = filtered_df["DUTY PAID_INR"].sum()
st.metric("Total Duty Paid (INR)", f"{total_duty:,.2f}")