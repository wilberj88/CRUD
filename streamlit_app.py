import streamlit as st
from streamlit_gsheets import GSheetsConnection
from st_paywall import add_auth
import streamlit.components.v1 as com


url = "https://docs.google.com/spreadsheets/d/1FLkogLFyJUc4fJX7T0LxkmQ2LJPwqvP46zA-9J_5L6E/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="Products")

st.header("Novus Mando 🎮 - Conexión GSheet Pública")
st.subheader("Chains 🏭🌎🚚 Inventory 📦 - Product Analysis")
st.dataframe(data)


st.subheader("Alarm Low Inventory 📦")
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

com.html("""
<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Subscribirme', '#29abe0', 'Q5Q8S0K6H');kofiwidget2.draw();</script> 
""")

add_auth(required=True)
# ONLY AFTER THE AUTHENTICATION + SUBSCRIPTION, THE USER WILL SEE THIS ⤵
# The email and subscription status is stored in session state.
st.write(f"Subscription Status: {st.session_state.user_subscribed}")
st.write("🎉 Yay! You're all set and subscribed to Novus! 🎉")
st.write(f'By the way, your email is: {st.session_state.email}')
