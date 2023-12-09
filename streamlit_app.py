import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1FLkogLFyJUc4fJX7T0LxkmQ2LJPwqvP46zA-9J_5L6E/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="0")

st.subheader("Novus Mando 🎮 - Chains 🏭🌎🚚 Inventory 📦")
st.dataframe(data)


st.subheader("Inventory Health Check 📦")
sql = '''
SELECT
  "Product_ID",
  "Product_Name",
  "Supplier",
  "Current_Inventory_Level",
  "Reorder_Level",
FROM
  Products
WHERE
  "Current_Inventory_Level" < "Reorder_Level"
ORDER BY
  "Reorder_Level" DESC;
'''
df_inventory_health = conn.query(spreadsheet=url, sql=sql)
st.dataframe(df_inventory_health)
