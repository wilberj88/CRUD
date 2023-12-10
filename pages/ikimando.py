import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#Title&Description
st.header("Novus Mando 🎮 - Conexión GSheet Privada")
st.subheader("🧠Iki❤️ ✍️ Inscripción")

#ConnectGoogleSheet
conn = st.connection("gsheets", type=GSheetsConnection)

#Formulario


st.subheader("🧠Iki❤️ 📁 BD")
#DataUsers
data = conn.read(worksheet="Users", usecols=list(range(6)), ttl=5)
data = data.dropna(how="all")
st.dataframe(data)


