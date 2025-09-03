# import password_generator_cli as pgc
from password_generator_cli import generate_password
import streamlit as st 

st.title("Password Generator App")
st.text("A simple web application to generate password.")

n_letters = st.number_input("How many letters needed in password", min_value=1, value=3)
n_numbers = st.number_input("How many numbers needed in password", min_value=1, value=3)
n_symbols = st.number_input("How many symbols needed in password", min_value=1, value=3)


if st.button("Generate Passsord"):
    password = generate_password(n_letters,n_numbers,n_symbols)
    st.write(f"Your generated password is {password}")
        
