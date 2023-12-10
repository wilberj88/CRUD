import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Users")

st.header("Novus Mando 🎮 - Conexión GSheet Privada")
st.subheader("🧠Iki❤️ 📁")

st.dataframe(data)


