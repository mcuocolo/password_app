import streamlit as st
from utils.qr_code import make_qr_code
from utils.password import Password

st.title("Personnal password generator")

password = ""
psw = Password()

with st.form("my_form"):
    st.subheader("Choose password options")
    psw.length = st.slider("Password length : ", min_value=4, max_value=32, value=12, step=2)
    col1, col2 = st.columns(2)
    #input widgets in 2 columns
    with col1:
        psw.allow_uppercase = st.checkbox("Allow UPPERCASE", value=True)
        psw.allow_symbols = st.checkbox("Allow symbols [!@#$%^&*()+]", value=True)
        psw.allow_similar = st.checkbox("Allow similar [iI1loO0]", value=True)
        
    with col2:
        psw.allow_lowercase = st.checkbox("Allow lowercase", value=True)
        psw.allow_numbers = st.checkbox("Allow numbers", value=True)
        psw.allow_duplicates = st.checkbox("Allow duplicates", value=True)

    submitted = st.form_submit_button('Generate')

if submitted:
    success, message, password = psw.generate_psw()
    if success:
        st.code(f"{password}")
        st.image(make_qr_code(password))
        
    else:
        st.write(message)

