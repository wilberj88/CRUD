import streamlit as st
from st-gsheets-connection import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1tW1NgWwTD-rWk8TYbA4NglQ9dwvKlm2Qrqn7nz9kULM/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecol=[0,1,2])

st.dataframe(data)
