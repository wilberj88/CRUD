import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1FLkogLFyJUc4fJX7T0LxkmQ2LJPwqvP46zA-9J_5L6E/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="0")

st.dataframe(data)
