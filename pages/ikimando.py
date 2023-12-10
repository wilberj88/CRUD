import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#Title&Description
st.header("Novus Mando 🎮 - Conexión GSheet Privada")

#ConnectGoogleSheet
conn = st.connection("gsheets", type=GSheetsConnection)

st.subheader("🧠Iki❤️ 📁 BD Actual")
#DataUsers
data = conn.read(worksheet="Users", usecols=list(range(7)), ttl=5)
data = data.dropna(how="all")
existing_data = data
st.dataframe(data)


st.subheader("🧠Iki❤️ ✍️ Inscripción")



#Formulario
ODS = [
    "ODS1_Pobreza",
    "ODS2_Hambre",
    "ODS3_Salud",
    "ODS4_Educación",
    "ODS5_Igualdad",
    "ODS6_Agua",
    "ODS7_Energía",
    "ODS8_Trabajo",
    "ODS9_Infraestructura",
    "ODS10_Desigualdades",
    "ODS11_Ciudades",
    "ODS12_Producción",
    "ODS13_Clima",
    "ODS14_VidaAcuática",
    "ODS15_Ecosistemas",
    "ODS16_Instituciones",
    "ODS17_Cooperación",
]
PAIDS = [
    "Saving Budget",
    "Earnings",
    "Comissions",
    "Saving Time",
    "Other",
]

# Onboarding New User MandIki Form
with st.form(key="user_form"):
    user_name = st.text_input(label="User Name*")
    user_email = st.text_input(label="User Email*")
    user_love = st.text_area(label="¿Qué te divierte? No te aburrirías de hacerlo casi todos los días")
    user_good = st.text_area(label="¿Para qué eres bueno? Agrega link de Linkedin del Rol al que aspiras")
    user_paid = st.multiselect("Por qué te pagarían", options=PAIDS)
    user_world_needs = st.selectbox("ODS que te mueve*", options=ODS, index=None)
    

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit New User Details")

    # If the submit button is pressed
    if submit_button:
        # Check if all mandatory fields are filled
        if not user_name or not user_email:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()
        elif existing_data["User_Name"].str.contains(user_name).any():
            st.warning("A user with this name already exists.")
            st.stop()
        else:
            # Create a new row of vendor data
            new_user_data = pd.DataFrame(
                [
                    {
                        "User_Name": user_name,
                        "User_Email": user_email,
                        "User_Love": user_love,
                        "User_Good": user_good,
                        "User_Paid": user_paid,
                        "User_World_Needs": user_world_needs,
                    }
                ]
            )

            # Add the new vendor data to the existing data
            updated_df = pd.concat([existing_data, new_user_data], ignore_index=True)

            # Update Google Sheets with the new vendor data
            conn.update(worksheet="Users", data=updated_df)

            st.success("User details successfully submitted! Bienvenido a MandIki")
            st.dataframe(updated_df)




