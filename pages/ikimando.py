import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, worksheet="Users")

st.subheader("Novus Mando 🎮 - 🧠Iki❤️")
st.subheader("Iki DB 📁")

st.dataframe(data)


