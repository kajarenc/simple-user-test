import streamlit as st

st.write(st.experimental_user.email)

st.write(st.experimental_user)

x = st.slider("X:", 0, 100, 5)
st.write(x**2)
