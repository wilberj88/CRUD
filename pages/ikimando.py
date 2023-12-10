import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Users")

st.header("Novus Mando 🎮 - Conexión GSheet Privada")
st.subheader("🧠Iki❤️ ✍️ Inscripción")


st.subheader("🧠Iki❤️ 📁 BD")
st.dataframe(data)


